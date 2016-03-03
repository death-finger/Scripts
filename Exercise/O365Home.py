from urllib import request, parse

url = parse.quote('http://www.microsoftstore.com.cn/类别/Office/Office-365-家庭版订阅---1-年新订或续订/p/6GQ-00089')
#print(url)
url = url[:4] + ':' + url[7:]
#print(url)
page = request.urlopen(url)
result = page.readlines()
for i in result[:21]:
    print(i.decode('utf-8'))
