#*-by using this we can use any no of parameter in a function and get result in tuple form
#**-duty same as single star, but the quality is high and the result in the form of dictinoary
#instead of method overloading  we use astra
def product(*args): #*arguments
    result=1 #start from
    for n in args:
        result*=n
    print(result)
product(1,2,3,4) #4 parameters
product(10,20) #2 parameters



#** program
def greeting(**kwargs):
    print(f"{kwargs.get('msg')}app user {kwargs.get('user_name')}")
greeting(msg="good mrng",user_name='kaavu')


######
def dispatch(**kwrgs):
    print(f"hello  {kwrgs.get('name')} your {kwrgs.get('food')}is ready to delivered ")
dispatch(food="burger",name="hana")
#purate double qoutes ullate konde ullil single qout



