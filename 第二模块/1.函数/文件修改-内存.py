
info = open('兼职白领学生空姐模特护士联系方式.txt','r+',encoding='utf-8')
data=info.read()
print(info.tell())
info.seek(0)
info.truncate()

new_str='zgd'
old_str='乔亦菲'


if old_str in data:
    line=data.replace(old_str,new_str)
info.write(line)

info.close()