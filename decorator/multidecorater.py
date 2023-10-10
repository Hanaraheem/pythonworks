#using 2 decorator
#order is must


def swap_nums(fl):  #first decorator
    def inner_fun(n1,n2): 
        if(n1<n2): 
            (n1,n2)=(n2,n1)
        return fl(n1,n2)
    return inner_fun

def smart_div(fl):  #2nd decorator
    def inner_fun(n1,n2):
        if n2==0:
            print("division is not possible")
            return
        return fl(n1,n2)
    return inner_fun

@swap_nums 
def sub(n1,n2):
    return n1-n2
                           
@swap_nums
@smart_div
def div(n1,n2):
    return n1/n2

print(sub(3,4))
print(div(5,0))


#program for order must

def decorator1(fn):
    def wrapper():
        print("decorator 1 before calling original function")#1st work
        result=fn()
        print("decorator 1 after calling original function")#5th work
        return result
    return wrapper

def decorator2(fn):
    def wrapper():
        print("decorator 2 before calling original function")#2nd work
        result=fn()
        print("decorator 2 after calling original function")#4rth
        return result
    return wrapper

@decorator1
@decorator2
def original_function():
    print("this is original function")#3rd

original_function()


##############
#in this program dec2 work first
def decor1(f):#f num() (first step)
    def inner():
        x=f() #20 (4rth) (ee step ullate konde aane deco2 poyi athe wrk aavunne)
        return x*x #20*20=400 (5th)
    return inner

def decor2(f):
    def inner():
        x=f()#x=10 (2 step)
        return x*x#2*10=20 (3 step)
    return inner

@decor1#2nd work
@decor2 #first work
def num():
    return 10
print(num())

###################
def italic_decoro(fn):
    def wrapper():
        result=fn()
        return f"<i>{result} </i>"
    return wrapper

def bold_decoro(fn):
    def wrapper():
        result=fn()
        return f"<b>{result} </b>"
    return wrapper

@italic_decoro
@bold_decoro
def greeting():
    return "good afternoon"

print(greeting())