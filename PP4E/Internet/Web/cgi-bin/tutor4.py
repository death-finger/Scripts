#!/usr/bin/python

import cgi, sys
sys.stderr = sys.stdout
form = cgi.FieldStorage()
print('Content-type: text/html\n')

html = """
<title>tutor4.py</title>
<h1>Greetings</h1>
<hr>
<h4>%s</h4>
<h4>%s</h4>
<h4>%s</h4>
<hr>"""

if not 'user' in form:
    line1 = 'Who are you?'
else:
    line1 = 'Hello, %s' % form['user'].value

line2 = "You're talking to a %s server" % sys.platform

line3 = ''
if 'age' in form:
    try:
        line3 = "Your age squared is %d!" % int(form['age'].value)**2
    except:
        line3 = "Sorry, I can't compute %s ** 2." % form['age'].value

print(html % (line1, line2, line3))