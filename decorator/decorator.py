#simple function
#low the redundancy ,reapeat aayite entelum function il vannal we use decorator
#eg:login 
#multiple decorotor use cheyyumbool order must aane
#rules
#1.function contain parameter as function
#2.another function on inside the function
#3.inside function parameter should be value

def swap_nums(fl): #parameter if an function
    def inner_fun(n1,n2): #inner function contain parameter as value     #DECORATOR FUNCTION
        if(n1<n2): #condition
            (n1,n2)=(n2,n1)#swapping
        return fl(n1,n2)
    return inner_fun

@swap_nums #decorator
def sub(n1,n2):
    return n1-n2
                           #NORMAL FUNCTION USING DECOROTOR
@swap_nums
def div(n1,n2):
    return n1/n2

print(sub(3,4))
print(div(4,2))



