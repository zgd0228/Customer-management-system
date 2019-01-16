
from tabulate import tabulate

staff = open('staff.db','r',encoding='utf-8')

regular = ['id','name','age','phone','dept','enroll_date']

def load_file(data):
    '''
    将文件内容转换成regular字典的格式
    '''
    set_data = {
        'id':[],
        'name':[],
        'age':[],
        'phone':[],
        'dept':[],
        'enroll_date':[]
    }
    for line in data:
        staff_id,staff_name,staff_age,staff_phone,staff_dept,staff_enroll = line.split(',')
        set_data['id'].append(staff_id)
        set_data['name'].append(staff_name)
        set_data['age'].append(staff_age)
        set_data['phone'].append(staff_phone)
        set_data['dept'].append(staff_dept)
        set_data['enroll_date'].append(staff_enroll)
    staff.close()
    return set_data

start=load_file(staff)

def print_log(mess,type_print = 'right'):
    if type_print == 'right':
        print('\033[34;0m %s \033[1m'%mess)
    elif type_print == 'error':
        print('\033[31;0m %s \033[1m'%mess)

def find_where(where):
    '''
    对分割的where语句进行分析，调用where_dict中的方法进行调用
    '''
    where_dict = {
        '>':gt,
        '<':lt,
        '=':eq,
        'like':like
    }
    for key,func in where_dict.items():
        if key in where:
            match_list,match_data = where.split(key)
            match_record = func(match_list.strip(),match_data.strip())
    return match_record

def gt(match_list,match_data):
    '''
    大于
    将匹配的复合条件的所有参数按照列表的形式返回给find_where
    [[],[],[],[]]
    '''
    list_age = []
    for i,j in enumerate(start[match_list]):
        if int(match_data)<int(j):
            new_list = []
            for t in start:
                new_list.append(start[t][i])
            list_age.append(new_list)
    return list_age

def lt(match_list,match_data):
    '''
    小于
    将匹配的复合条件的所有参数按照列表的形式返回给find_where
    [[],[],[],[]]
    '''
    list_age = []
    for i,j in enumerate(start[match_list]):
        if int(match_data)>int(j):
            new_list = []
            for t in start:
                new_list.append(start[t][i])
            list_age.append(new_list)
    return list_age

def eq(match_list,match_data):
    '''
    等于
    将匹配的复合条件的所有参数按照列表的形式返回给find_where
    [[],[],[],[]]
    '''
    list_age = []
    for i,j in enumerate(start[match_list]):
        if match_data==j:
            new_list = []
            for t in start:
                new_list.append(start[t][i])
            list_age.append(new_list)
    return list_age

def like(match_list,match_data):
    '''
    like语句
    将匹配的复合条件的所有参数按照列表的形式返回给find_where
    [[],[],[],[]]
    '''
    list_age = []
    for i,j in enumerate(start[match_list]):
        if match_data in j:
            new_list = []
            for t in start:
                new_list.append(start[t][i])
            list_age.append(new_list)
    return list_age

def find(cmd,data):
    '''
    按照条件查找数据,将从find_where得到的数据按照条件进一步进行提取
    eg:from_before = [' name','age ']
    from_new = ['name','age']
    new_list= [[],[],[],[]]
    '''
    from_before = cmd.split('from')[0][4:].split(',') #提取关键字
    from_new =[j.strip() for j in from_before ]  #去空格
    if "*" in from_new:
        print(tabulate(data,headers=regular,tablefmt="grid"))
    else:
        new_list = []
        for i in data:
            re_list = []
            for mess in from_new:#regular.index([mess])按照元素在regular的位置找到对应的索引
                #print(regular.index(mess))
                re_list.append(i[regular.index(mess)])
            new_list.append(re_list)
        print(new_list,tabulate(new_list,headers=from_new,tablefmt="grid"))
    print_log('影响了%s条数据'%len(data),'right')

def add(cmd,data):
    '''
    增加数据,进行自加 1 排序，将排序添加到信息的开头。
    逐一将列表中的数据按照regular的排列位置添加到对相应的start字典的列表中
    regular[x] = start.keys()
    start.get(regular[x]) :表示从第一个key值得到对应的value值，并将对应的参数添加进去
    '''
    mess = cmd.split('staff_table')
    mess_list = mess[1].strip().split(',')
    index = int(start['id'][-1]) + 1
    mess_list.insert(0,str(index))
    if mess_list[3] not in start['phone']:   #判断电话号码是否重复
        x = 0
        for i in mess_list:
            start.get(regular[x]).append(str(i))
            x += 1
        write_file()
    else:
        print('电话号码有误，已存在')

def delt(cmd,data):
    '''
    按照索引删除数据  del id = 3
    删除后重新排序，id= [1,2,4,5,...]
                    id = [1,2,3,4....]
    '''
    for i in data:
        i_index = i[0]    #取个人信息中的排序
        finall_index = start['id'].index(i_index)  #得到排序在字典的value中的索引
        for r in start:   #r = key
            start.get(r).pop(finall_index)  #将每个key对应的value中按照索引删除元素
        index = []
        t = 0
        for  x in start['id'][finall_index:]:   #按照id删除后，对id重新排序
            x = int(x)-1
            start['id'][finall_index+t] = str(x)
            t += 1
    write_file()

def update(cmd,data):
    '''
    通过调用从find_where中传递过来的条件，按照条件进行替换
    '''
    set_after = cmd.split('set')[1]
    if len(set_after)>1:
        set_data,set_new = set_after.strip().split('=')
        for mess in data:
            mess_index = mess[0]
            finall_index = start['id'].index(mess_index)  #找到条件在字典中对应的索引
            start[set_data][finall_index] = set_new   #找到要替换的参数的位置，将其替换
    else:
        print_log('语法错误','error')
    print_log('影响了%s条数据'%len(data),'right')
    write_file()

def write_file():
    '''
    将字典中的数据写到文件中
    '''
    staff_1 = open('staff.new','w',encoding='utf-8')
    for index,mess in enumerate(start['id']):
        record = []
        for i in regular:
            record.append(start[i][index])
        staff_1.write(','.join(record))
    staff_1.close()

def think(cmd):
    '''
    对命令语句进行分析，首先判断命令是否以find，add，del，update这四个关键字开头
    然后判断是否有关键字where，将有关键字where的命令进行拆分，没有where进行重新构造。然后统一调用方法
    data：为find_where()的返回值
    where_before: 为cmd中where之前的语句
    '''
    main_list = {
        'find':find,
        'add':add,
        'del':delt,
        'update':update
    }
    if cmd.split()[0] in main_list.keys():
        if 'where' in cmd:
            where_before,where_after = cmd.split('where')
            data=find_where(where_after)
        else:
            data = []
            for index,mess in enumerate(start['id']):   #[0 1][1 2][2 3][3 4][4 5]
                record = []
                for mess1 in regular:
                    record.append(start[mess1][index])
                data.append(record)
                where_before = cmd
        match_first = cmd.split()[0]
        for key,func in main_list.items():
            if key == match_first:
                func(where_before,data)
    else:
        print_log('语法错误，缺少关键字开头','error')

def main():
    '''
    主函数
    '''
    while True:
        cmd = input('[cmd]>>>').strip()
        if not cmd:continue
        think(cmd)

main()