#!/usr/bin/python


"""
实现用来查看和更新保存在shelve中类实例的基于Web的界面;
shelve保存在服务器上
"""

import cgi, shelve, sys, os                             # cgi.test()转储输入
shelvename = 'class-shelve'                             # shelve文件在当前工作目录
fieldnames = ('name', 'age', 'job', 'pay')

form = cgi.FieldStorage()                               # 解析表单数据
print('Content-type: text/html')                        # 响应HTML中的hdr和空行
sys.path.insert(0, os.getcwd())

# main Html template
replyhtml = """
<html>
<title>People Input Form</title>
<body>
<form method="POST" action="peoplecgi.py">
    <table>
        <tr><th>key<td><input type="text" name="key" value="%(key)s" </td></th></tr>
        $ROWS$
    </table>
    <p>
        <input type="submit" value="Fetch", name="action">
        <input type="submit" value="Update", name="action"
    </p>
</form>
</body>
</html>
"""

# Insert $ROWS$ into html
rowhtml = '<tr><th>%s<td><input type="text" name=%s value="%%(%s)s">\n </td></th></tr>'
rowshtml = ''
for filedname in fieldnames:
    rowshtml += (rowhtml % ((fieldname,) * 3))
replyhtml = replyhtml.replace('$ROWS$', rowshtml)

def htmlize(adict):
    new = adict.copy()
    for field in fieldnames:
        value = new[field]
        new[field] = cgi.escape(repr(value))
    return new

def fetchRecord(db, form):
    try:
        key = form['key'].value
        record = db[key]
        fields = record.__dict__
        fields['key'] = key
    except:
        fields = dict.fromkeys(fieldnames, '?')
        fields['key'] = 'Missing or invalid key!'
    return fields

def updateRecord(db, form):
    if not 'key' in form:
        fields = dict.fromkeys(fieldnames, '?')
        fields['key'] = 'Missing key input!'
    else:
        from person import Person
        record = Person(name='?', age='?')
        for field in fieldnames:
            setattr(record, field, eval(form[field].value))
        db[key] = record
        fields = record.__dict__
        fields['key'] = key
    return fields

db = shelve.open(shelvename)
action = form['action'].value if 'action' in form else None
if action == 'Fetch':
    fields = fetchRecord(db, form)
elif action == 'Update':
    fields = updateRecord(db, form)
else:
    fields = dict.fromkeys(fieldnames, '?')
    fields['key'] = 'Missing or invalid action!'
db.close()
print(replyhtml % htmlize(fields))
