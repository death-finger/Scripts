import re

pattern, string = 'A.C.', 'xxABCDxx'
matchobj = re.search(pattern, string)
if matchobj:
    print(matchobj.start())

pattobj = re.compile('A.*C.*')
matchobj =