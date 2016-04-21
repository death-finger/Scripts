# e.g. 13-29

import sys, http.client
showlines = 6

try:
    servername, filename = sys.argv[1:]
except:
    servername, filename = 'www.sina.com.cn', '/index.html'

print(servername, filename)
server = http.client.HTTPConnection(servername)
server.putrequest('GET', filename)
server.putheader('Accept', 'text/html')
server.endheaders()

reply = server.getresponse()
print(reply.status)
if reply.status != 200:
    print('Error sending request', reply.status, reply.reason)
else:
    data = reply.readlines()
    reply.close()
    for line in data[:showlines]:
        print(line)