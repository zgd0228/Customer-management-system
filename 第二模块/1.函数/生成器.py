#l列表生成式
# a = list(range(10))
#
# a = [i if i<4 else i*i for i in a]
# print


#生成器
# a = list(range(10))
# a = (i if i<4 else i*i for i in a)
# print(a)
#
# print(next(a))
# print(next(a))


#函数生成器

# def func(max):
#     n,a,b = 0,0,1
#
#     while n<max:
#         yield b
#         a,b = b,a+b
#         n = n+1
#     return 'done'
#
# f = func(15)
# for i in f:
#     print(i)

from functools import wraps
def wrapper(func):
    @wraps(func)
    def inner():
        print(func.__name__)
        return func()
    return inner

@wrapper
def work():
    return 123

print(work.__name__)
work()


