# def login(func):
#     def inner(*args,**kwargs):
#         username = 'zgd'
#         password = 'zgd123'
#         us =input('>>>').strip()
#         pd = input(">>>").strip()
#         if username == us and password == pd:
#             func(*args,**kwargs)
#     return inner
#
# @login
# def func():
#     print('success')
#
# func()

def login(args):
    def outer(func):
        def inner(*args,**kwargs):
            username = 'zgd'
            password = 'zgd123'
            us =input('>>>').strip()
            pd = input(">>>").strip()
            if username == us and password == pd:
                func(*args,**kwargs)
        return inner
    return outer

@login('qq')
def func(x):
    print('success',x)

func('hh')