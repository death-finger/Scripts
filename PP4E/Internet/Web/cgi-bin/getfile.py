#!/usr/bin/python

import cgi, os, sys
formatted = True
privates = ['PyMailCgi/cgi-bin/secret.py']


try:
    samefile = os.path.samefile
except:
    def samefile(path1, path2):
        apath1 = os.path.abspath(path1).lower()
        apath2 = os.path.abspath(path2).lower()
        return apath1 == apath2

html = """
<html><title>Getfile response</title>
<h1>Source code for: '%s'</h1>
<hr>
<pre>%s</pre>
<hr></html>"""

def restricted(filename):
    for path in privates:
        if samefile(path, filename):
            return True

try:
    form = cgi.FieldStorage()
    filename = form['filename'].value
except:
    filename = 'cgi-bin/getfile.py'

try:
    assert not restricted(filename)
    filetext = open(filename).read()
except AssertionError:
    filetext = '[FILE ACCESS DENIED]'
except:
    filetext = '(Error opening file: %s)' % sys.exc_info()[1]

if not formatted:
    print('Content-type: text/plain\n')
    print(filetext)
else:
    print('Content-type: text/html\n')
    print(html % (filename, cgi.escape(filetext)))

