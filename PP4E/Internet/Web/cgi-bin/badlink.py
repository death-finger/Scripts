#!/usr/bin/python
import cgi, sys
form = cgi.FieldStorage()


for name in form.keys():
    print('[%s:%s]' % (name, form[name].value), end=' ', file=sys.stderr)
