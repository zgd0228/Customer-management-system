login_flag = False
def login(func):
    def inner(*args,**kwargs):
        us = 'zgd'
        pd = 'zgd123'
        global login_flag
        if login_flag == False:
            us_ = input('>>>')
            pd_ = input('>>>')
            if us == us_ and pd == pd_:
                login_flag = True

        else:
            print('用户已经登录')
        if login_flag == True:
            func(*args,**kwargs)
    return inner

def ribben():
    print('-----ribrn-----')
def china():
    print('-----china-----')
@login
def us():
    print('-----us-----')
@login
def henan(style):
    print('-----henann-----',style)
def hongkong():
    print('-----hongkong-----')

henan('hh')
us()
