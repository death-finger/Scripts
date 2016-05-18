import re

pattern, string = 'A.C.', 'xxABCDxx'
matchobj = re.search(pattern, string)
if matchobj:
    print(matchobj.start())

pattobj = re.compile('A.*C.*')
matchobj = pattobj.search('xxABCDxx')
if matchobj:
    print(matchobj.start())

print(re.search(' *A.C[DE][D-F][^G-ZE]G\t+ ?', '..ABCDEFG\t..').start())
