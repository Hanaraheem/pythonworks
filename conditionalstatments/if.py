#conditional statements
#comparison ,relational,logical are used
#if ,if else,elif
#tap space are used instead of curly brackets,:should needed intentation
#if  body not should be empty
 

#if syntax
#if (condition)
#    statment


#check a number is positive

num=5
if(num>0):
    print()
    print("given number is positive.." )
    print("hello")  #inside the if statement
print("hi")#outside the  if statement
if(num<0):
    print("given number is negative...")

#find the greater number using if statement only

a=20
b=10
if a>b:
    print("largest number =",a)
if(a<b):
     print("largest number =",b)


#from the user input we used typeinput("")
#int(input)

num1=int(input("enter the first number:"))  
num2=int(input("enter the second number:"))   #type gave fo getting value
print(type(num1))
print(type(num2))
print(num1*10)





num1=(input("enter the first number:"))
num2=(input("enter the second number:"))    #string  by defult
print(num1)
print(num2)


#float(input)

num1=float(input("enter the first number:"))  
num2=float(input("enter the first number:")) 
print(type(num1))
print(type(num2)) 




#voting eligiblility
age=int(input("enter your age:"))
if(age>=18):
    print("eligilible for voting")
if(age<18):
    print("not eligilible for voting")


# question:read colour from user if red =print "stop",green=print "go",yellow=print  "wait"

colour=(input("enter the colour:"))
if(colour=="red"):
        print("stop")
if(colour=="green"):
        print("go")
if(colour=="yellow"):
        print("wait")


    
 