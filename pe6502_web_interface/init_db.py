import os
import sqlite3


class InitDb:
    def __init__(self):
        os.mkdir("pe6502_web_interface/data") if not os.path.isdir(
            "pe6502_web_interface/data"
        ) else None
        db = sqlite3.connect("pe6502_web_interface/data/data.db")
        db.cursor().execute(
            "create table if not exists programs (id INTEGER PRIMARY KEY, created_at integer,updated_at integer,description,content,is_deleted integer default 0);"
        )
        db.commit()
