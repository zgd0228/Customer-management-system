'''修改用户信息'''
info = open('account.txt','r+',encoding='utf-8')
data = info.readlines()
info1 = {}
for line in data:
    line = line.strip()
    if not line.startswith('!'):
        items = line.split(',')
        info1[items[0]] = items

def mess_write():
    info.seek(0)
    info.truncate()
    for i in info1.values():

        str_persons = ','.join(i)
        info.write('%s\n'%str_persons)

    info.flush()

def print_mg(username,info1):
    mg = info1.get(username)
    info = '''
    -----------------------
    1、name:%s
    2、full name:%s
    3、age:%s
    4、job:%s
    5、position:%s
    6、phone:%s
    -----------------------'''%(username,mg[2],mg[3],mg[4],mg[5],mg[6])
    print(info)
def modify_mg(username,info1):
    mg = info1.get(username)
    for index,value in enumerate(mg):
        if index > 1:
            print(index,value)
    choice1 = input('修改选项：')
    if choice1.isdigit():
        choice1 = int(choice1)
        if choice1 < len(mg):
            person_old = mg[choice1]
            input_pmg = input('输入新的信息')
            person_new = person_old.replace(person_old,input_pmg)
            mg[choice1] = person_new
            print('修改成功')

def modify_ps(username,info1):
    password=info1.get(username)[1]
    pd = input('旧密码')
    if pd == password:
        password_change = input('输入新密码:')
        password_change1 = input('再输入新密码:')
        if password_change == password_change1:
            password_new = password.replace(password,password_change)
            info1.get(username)[1] = password_new
            print('密码修改成功')
        else:
            print('密码输入错误')
    else:
        print('密码输入错误')

mg = '''
    1、打印用户信息
    2、修改个人信息
    3、修改密码'''
count=0
while count<3:
    username = input('输入用户名：').strip()
    password = input('输入用户密码：').strip()
    pwd = info1.get(username)[1]
    if pwd == password:
        print(('welcome %s'%username).center(50,'-'))
        while True:
            print(mg)
            choice = input('>>>').strip()
            if choice.isdigit():
                choice = int(choice)
                if 0 < choice < 4:
                    if choice == 1:
                        print_mg(username,info1)
                    elif choice == 2:
                        modify_mg(username,info1)
                    else:
                        modify_ps(username,info1)
                else:
                    print('你的输入有误,该选项不存在')
            elif choice == 'q':
                mess_write()
                info.close()
                exit()
            else:
                print('你的输入有误')
    else:
        print('你的用户名或密码错误')

