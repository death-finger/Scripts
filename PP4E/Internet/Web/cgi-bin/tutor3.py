#!/usr/bin/python

import cgi
form = cgi.FieldStorage()
print('Content-type: text/html')

html = """
<title>tutor3.py</title>
<h1>Greetings</h1>
<hr>
<p>%s</p>
<hr>"""

if not 'user' in form:
    print(html % 'Who are you?')
else:
    print(html % ('Hello, %s.' % form['user'].value))

