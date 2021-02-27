%rebase("pe6502_web_interface/_template.tpl")
<h2>Edit row id: {{rows[0][0]}}</h2>
<p><a href="/">Go Back</a></p>
<form action="/edit" method="POST">
  %for row in rows:
  <div class="form-group">
    <label for="inputDescription">Description</label>
    <input name="description" value="{{row[1]}}" type="text" class="form-control" id="inputDescription" placeholder="Description or title">
  </div>
  <div class="form-group">
    <label for="inputContent">Example textarea</label>
    <textarea name="content" class="form-control" id="inputContent" rows="10">{{row[2]}}</textarea>
  </div>
  <input type="hidden" name="id" value="{{row[0]}}">
  <button type="submit" class="btn btn-primary">Submit</button>
</form>


