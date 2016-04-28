#!/usr/bin/python

import cgi, sys
form = cgi.FieldStorage()
print('Content-Type: text/html\n')

html = """
<title>tutor5.py</title>
<h1>Greetings</h1>
<hr>
<h4>Your name is %(name)s</h4>
<h4>You wear rather %(shoesize)s shoes</h4>
<h4>Your current job: %(job)s</h4>
<h4>You program in %(language)s</h4>
<h4>You alse said:<h4>
<p>%(comment)s</p>
<hr>"""

data = {}
for field in ('name', 'shoesize', 'job', 'language', 'comment'):
    if not field in form:
        data[field] = "(unknown)"
    else:
        if not isinstance(form[field], list):
            data[field] = form[field].value
        else:
            values = [x.value for x in form[field]]
            data[field] = ' and '.join(values)

print(html % data)