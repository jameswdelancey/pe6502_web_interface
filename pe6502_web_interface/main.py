import sqlite3

import serial
from bottle import debug, redirect, request, route, run, static_file, template

from init_db import InitDb

InitDb()

SERIAL_PORT = "/dev/ttyUSB0"
db = sqlite3.connect("pe6502_web_interface/data/data.db")


def get_from_serial():
    data = s.readline().decode().replace("\r", "\r\n")
    acc = []
    while data:
        acc += [data]
        data = s.readline().decode().replace("\r", "\r\n")
    return "".join(acc)


@route("/")
def hello():
    return template(
        "pe6502_web_interface/tasks.tpl",
        rows=db.cursor()
        .execute("select id,description from programs where is_deleted!=1")
        .fetchall(),
    )


@route("/static/<path:path>")
def help(path):
    assert path
    return static_file(path, root="pe6502_web_interface/static/")


@route("/new", method="GET")
def new_item():
    return template("pe6502_web_interface/new_task.tpl")


@route("/new_fr_serial", method="GET")
def new_from_serial():
    """Creates a new programs entry from the device

    This is a minimum viable product for this method and has no saftey for
    santizing the input which should be added before allowing public network
    access.
    """
    assert request.params.dict.keys() == {"cmd"}
    CMD_TO_START_READ = request.params.getone("cmd")
    get_from_serial()
    s.write((CMD_TO_START_READ + "\r").encode())
    # breakpoint()
    try:
        content = "\r\n".join(get_from_serial().splitlines()[1:])
    except Exception:
        content = "No text returned from device."
    try:
        db.cursor().execute(
            "insert into programs (description,content) values(?,?)",
            ("No description entered.", content),
        )
        db.commit()
    except Exception as e:
        return f'<p>{e!r}</p><br><a href="/">Go Back</a>'

    return redirect("/")


@route("/new", method="POST")
def new_item():
    """Creates a new item for a program in the database

    Be aware that this has hard coded debugging in it and is not intended to be
    used on a public-facing network. Additionally some CSRF and login logic
    will be needed to upgrade this to work on a public network.
    """
    assert request.forms.dict.keys() == {"description", "content"}
    try:
        db.cursor().execute(
            "insert into programs (description,content) values(?,?)",
            (request.forms.getone("description"), request.forms.getone("content")),
        )
        db.commit()
    except Exception as e:
        return f'<p>{e!r}</p><br><a href="/">Go Back</a>'

    return redirect("/")


@route("/edit/<id:int>", method="GET")
def edit_item(id):
    return template(
        "pe6502_web_interface/edit_task.tpl",
        rows=db.cursor()
        .execute("select id,description,content from programs where id=?", (id,))
        .fetchall(),
    )


@route("/edit", method="POST")
def edit_item():
    """Edits an item for a program in the database

    Be aware that this has hard coded debugging in it and is not intended to be
    used on a public-facing network. Additionally some CSRF and login logic
    will be needed to upgrade this to work on a public network.
    """
    assert request.forms.dict.keys() == {"description", "content", "id"}
    try:
        db.cursor().execute(
            "update programs set description=?,content=? where id=?",
            (
                request.forms.getone("description"),
                request.forms.getone("content"),
                request.forms.getone("id"),
            ),
        )
        db.commit()
    except Exception as e:
        ret = f'<p>{e!r}</p><br><a href="/">Go Back</a>'
    else:
        ret = template(
            "pe6502_web_interface/tasks.tpl",
            rows=db.cursor()
            .execute("select id,description from programs where is_deleted!=1")
            .fetchall(),
        )
    return ret


@route("/del/<id:int>", method="GET")
def del_item(id):
    try:
        db.cursor().execute(
            "update programs set is_deleted=1 where id=?",
            (id,),
        )
        db.commit()
    except Exception as e:
        ret = f'<p>{e!r}</p><br><a href="/">Go Back</a>'
    else:
        ret = template(
            "pe6502_web_interface/tasks.tpl",
            rows=db.cursor()
            .execute("select id,description from programs where is_deleted!=1")
            .fetchall(),
        )
    return ret


@route("/run/<id:int>", method="GET")
def run_item(id):
    """Runs a program from a line in the database

    This method works by typing the text verbatim therefore the context of the
    computer will need to be set beforehand, such as running 'new' in BASIC or
    entering the correct interpreter or WozMon.
    """
    assert (
        db.cursor()
        .execute("select count(*) from programs where id=?", (id,))
        .fetchone()
    )

    send = (
        db.cursor()
        .execute("select content from programs where id=?", (id,))
        .fetchone()[0]
        .replace("\r\n", "\r")
        .replace("\n", "\r")
    )
    s.write((send + "\r").encode())
    return redirect("/")


with serial.Serial(SERIAL_PORT, 115200, timeout=0.5, rtscts=1) as s:
    run(host="0.0.0.0", port=8080, debug=True, reloader=True)
