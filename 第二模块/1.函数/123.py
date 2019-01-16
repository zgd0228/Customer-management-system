staff = open('staff.db','r+',encoding='utf-8')
info={}

for line in staff.readlines():
    staff_list = line.strip().split(',')
    info[staff_list[0]]=staff_list[1:]
new_list = []


for i,j in info.items():

    new_list=j

    new_list.insert(0,i)
    print(new_list)