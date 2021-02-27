%rebase("pe6502_web_interface/_template.tpl")
<h2>Add New</h2>
<p><a href="/">Go Back</a></p>
<form method="POST">
  <div class="form-group">
    <label for="inputDescription">Description</label>
    <input name="description" type="text" class="form-control" id="inputDescription" placeholder="Description or title">
  </div>
  <div class="form-group">
    <label for="inputContent">Example textarea</label>
    <textarea name="content" class="form-control" id="inputContent" rows="10"></textarea>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
<br>
<form action="/new_fr_serial">
  <div class="form-group">
    <label for="inputNewFromSerial">Add New from Serial</label>
    <input name="cmd" type="text" class="form-control" id="inputCmd" value="LIST">
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
<form>

