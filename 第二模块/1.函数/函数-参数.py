#
# #默认参数
# def run(name,age,sex,country='CN'):
#     info='''
#     ---------info---------
#     name:%s
#     age:%s
#     country:%s
#     sex:%s
#     '''%(name,age,country,sex)
#     print(info)
# run('zgd',22,'man')
# run('alex',33,'women','afica')
#
#
# #关键参数
# def run(name,age,sex,country='CN'):
#     info='''
#     ---------info---------
#     name:%s
#     age:%s
#     country:%s
#     sex:%s
#     '''%(name,age,country,sex)
#     print(info)
# run('zgd',22,'man')
# run('alex',33,country='afica',sex='women')

#非固定参数
# def run(mql,*args):
#     for i in args:
#         print('%s 接收到一条 %s 消息!'%(i,mql))
#
# run('huozai','zgd','alex','peiqi')

def run(mql,*args,age):
    for i in args:
        print('%s 接收到一条 %s 消息!%s'%(i,mql,age))

run('huozai',*['zgd','alex','peiqi'],age=22)