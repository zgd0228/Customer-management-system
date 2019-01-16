'''修改用户信息'''
info = open('account.txt','r+',encoding='utf-8')
data = info.readlines()
info1 = {'shanshan': ['shanshan', 'ss123', '杜姗姗', '22', 'Model', 'PR', '13834561230'], 'alex': ['zgd', 'abc123', 'Alexander Li', '222', 'CEO', 'IT', '13332228888'], 'rain': ['rain', 'rain123', 'RainWang', '27', ' Engineer ', 'IT ', '133542453453']}
for line in data:
    line = line.strip()
    if not line.startswith('!'):
        items = line.split(',')
        info1[items[0]] = items
def mess_write():
    info.seek(0)
    info.truncate()
    for i in info1.values():
        print(i)
        str_persons = ','.join(i)
        info.write(str_persons)
