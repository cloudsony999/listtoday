def f1():
    pass
x=f1()
print(type(x))

def f2():
    return 100

print(f2())

def f3(x):
    return x,100

print(f3(23))
print(f3('kushal'))

name='kushal'
title='ghosh'

print("my full name is {} {}".format(name,title))

def print_fullname(name,title):
    print("my full name is {} {}".format(name,title))

print_fullname('amitava','chatterjee')

def print_fullname_modified(name,title):
    return f"my full name is {name} {title}"

print(print_fullname_modified('priyam','acharya'))

