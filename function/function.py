#block of code-function
#it is for task perform  eg:print,round,input,max,sum,sorted,min
#def use in python for function
#call cheyyan vendi(eg:addition)
#call parameter-arguments
# #syntax:def_function name(parameter)
# #if we want to get the output we should gave input on outside the function

# def sum(a,b):
#     s=a+b
#     print(s)

# sum(2,5)

      #or function with return
def add(n1,n2):
   result=n1+n2
   return result

print(add(40,50))

#cube

def cube(a):
   res=a**2
   return res

print(cube(3))

# #multiplication

# def multi(a,b):
#     m=a*b
#     print(m)

# multi(2,5)

# #sub
# def sub(a,b):
#     sub=a-b
#     print(sub)

# sub(2,5)



# #user input

# def sum(a,b):
#     s=a+b
#     m=a*b
#     sub=a-b
#     print(s)
#     print(m)
#     print(sub)

# num1=int(input("enter the number:"))  
# num2=int(input("enter the number:"))
# sum(num1,num2)


#odd or even

def number(a):
    if(a%2!=0):
     print("it is odd")
    else:
        print("it is even")

n=int(input("enter the number:"))
number(n)



#largest of 3 numbers

# num1=int(input("enter the number1:"))
# num2=int(input("enter the number2:"))
# num3=int(input("enter the number3:"))
# def largest(a,b,c):
#    if a>b and a>c:
#         print(a)
#    elif b>a and b>c:
#        print(b)
#    elif c>a and c>b:
#       print(c)
    
# largest(num1,num2,num3) 


#count vowels and consonants in string


text=str(input("enter the word:"))

def count(a):
    v_count=0
    c_count=0
    for i in range(len(a)):
     if a[i] in ["a","e","i","o","u"]:
       v_count+=1
    else:
        c_count+=1

    print("vowel count",v_count)
    print("consanant count",c_count)


count(text)

#area of circle

radius=float(input("enter the radius"))
def area(a):
   area=(3.14*radius**2)
   print(area)
area(radius)


# def sum() #if we have no statements we use pass statement to remove error
#    pass

#return keyword
#return value 
# using return keyword before the print fuction

radius=float(input("enter the radius"))
def area(a):
   area=(3.14*radius**2)
   return area  # use return keyword only inside the function to print outside

print(area(radius))#return help to print together



#largest of two numbers

num1=int(input("enter the number1:"))
num2=int(input("enter the number2:"))
def largest(a,b):
    if (a>b ):
       return print(a)
    else:                    # we can also use this statement instead of this return n1 if n1>n2 else n2  
      return print(b)

       
print(largest(num1,num2))


#or
def max(n1,n2):
   return  n1 if n1>n2 else n2  
print (max(50,100))


#sub

def sub(n1,n2):
    return n1-n2
    

print(sub(2,5))

#smart sub-the output not should be negative (either n1 or n2 can be smaller or larger but the result  should be always positive)

def smart_sub(n1,n2):
   return n1-n2 if n1>n2 else n2-n1

print(smart_sub(10,5))
print(smart_sub(5,10))


#odd or even

def number(n):
   return  "odd" if n%2!=0  else "even"

print(number(10))



#hcf

def hcf(num1,num2):
   res=1
   sm_num=num1 if  num1<num2 else num2
   for i in range(1,sm_num-1):
      if num1%i==0 and num2%i==0:
         res=i
   return res
print(hcf(18,24))
      
# num1=int(input("enter the n1:"))
# num2=int(input("enter the n1:"))
# print(hcf(num1,num2))



#lcm(logic)=lcm(num1,num2)=num1*num2/hcf(num1,num2)

def lcm(num1,num2):
   gcd=hcf(num1,num2)
   res=(num1*num2)/gcd
   return res
print(lcm(18,24))



    #or (without equation)

def lcm(n1,n2):
 max=n1 if n1>n2 else n2
 flag=True
 while(flag):
     if(max %n1==0) and (max%n2!=0):
        print("lcm ",n1,n2 is max)
        break
     else:
        max=max+1
lcm(18,24)




#get dis price  
# 50 ,20
# 10 discount
# 50-10=40  selling price

def get_discount_price(actual_price,discount):
   selling_price=actual_price - (actual_price*discount)/100
   return selling_price

print( get_discount_price(50,10))



