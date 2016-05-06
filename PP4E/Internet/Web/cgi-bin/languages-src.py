#!/usr/bin/python

import cgi


filename = 'cgi-bin/languages.py'
print('Content-type: text/html\n')
print('<title>Languages</title>')
print('<h1>Source code: "%s"</h1>' % filename)
print('<hr><pre>')
print(cgi.escape(open(filename).read()))
print('</pre><hr>')
