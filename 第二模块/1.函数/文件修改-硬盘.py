import os

op_file='兼职白领学生空姐模特护士联系方式.txt'
new_op='%s new'%op_file
info = open(op_file,'r',encoding='utf-8')
info1 = open(new_op,'w',encoding='utf-8')
new_str='zgd'
old_str='乔亦菲'

for line in info:
    if old_str in line:
        line=line.replace(old_str,new_str)
    info1.write(line)

info.close()
info1.close()
os.rename('兼职白领学生空姐模特护士联系方式1.txt','兼职白领学生空姐模特护士联系方式.txt')

