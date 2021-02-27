%rebase("pe6502_web_interface/_template.tpl")
          <h2>Content</h2>
          <p><a href="/new">Add New</a><p>
          <div class="table-responsive">
            <table class="table table-striped table-sm">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Description</th>
                  <th></th>
                </tr>
              </thead>
              <tbody>
                %for row in rows:
                <tr>
                  %for col in row:
                  <td>{{col}}</td>
                  %end
                  <td>
                    <a href="/edit/{{row[0]}}">Edit</a>
                    <a href="/del/{{row[0]}}">Del</a>
                    <a href="/run/{{row[0]}}">Run</a>
                  </td>
                </tr>
                %end
              </tbody>
            </table>
          </div>
