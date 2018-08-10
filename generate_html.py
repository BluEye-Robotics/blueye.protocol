#!/usr/bin/env python3
import json
import html
import os
jdata = json.loads(open("protocol.json").read())

doc = """<!DOCTYPE html>
<html lang="en">
<head>
  <title>TCP protocol</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js"></script>
</head>
<body>

<div class="container">"""
for version in jdata:
    for message in version['messages']:
        ###show = "show" if n == len(jdata.keys()) - 1 else ""
        show = ""
        ver = version['version']
        doc += """
        <div class="card">
          <div class="card-header">
            <a class="card-link" data-toggle="collapse" href="#collapse%s">
            Protocol version %s %s
            </a>
          </div>
          <div id="collapse%s" class="collapse %s" data-parent="#accordion">
            <div class="card-body">

          <table class="table table-striped">
          <thead>
            <tr>
              <th scope="col">Field</th>
              <th scope="col">Type</th>
              <th scope="col">Unit</th>
              <th scope="col">Description</th>
            </tr>
          </thead>
          <tbody>
        """ % (ver + message['message_type'], ver, message['name'], ver + message['message_type'], show)
        for field in message["fields"]:
            doc += """    <tr>
              <th scope="row">%s</th>
              <td>%s</td>
              <td>%s</td>
              <td>%s</td>
            </tr>""" % (html.escape(field['field_name']),
                        html.escape(field['dtype']),
                        html.escape(field['unit']),
                        html.escape(field['description']))

        doc += """ </tbody>
          </table>
          </div>
        </div>
      </div>
          """

doc += """</div>

</body>
</html>
"""

with open(os.path.join("html", "protocol.html"), "w") as f:
    f.write(doc)
