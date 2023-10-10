# grading system
# > 90-A+
# > 80-A
# > 70-B+
# > 60-B
# > 50-C+
# > 40-C
# > 30-D+
# > 30-Failed

#using if elif else

mrk=int(input("enter the mark:"))
if(mrk>=90):    
    print("A+")
elif(mrk>=80):
    print("A")
elif(mrk>=70):
    print("B+")
elif(mrk>=60):
    print("B")
elif(mrk>=50):            
    print("C+")
elif(mrk>=40):
    print("C")
elif(mrk>=30):
     print("D+")
else:
  print("failed")



    


    #grade enter and print which category of mark it is.

# grade=(input("enter the grade:"))
# if(grade==A+):
#     print("above 90")
# elif(grade==A):
#      print("between 90-80")
# elif(grade==B+):
#      print("between 80-70")
#  elif(grade==B):
#      print("between 70-60")
#  elif(grade==C+):            
#      print("between 60-50")
#  elif(grade==C):
#      print("between 50-40")
#  elif(grade==D+):
#      print("below 30")
# else:
#      print("failed")


   
 

# program to find largest of 3 numbers


print("enter the 3 numbers")
num1=int(input("num1"))
num2=int(input("num2"))
num3=int(input("num3"))
if num1>num2 and num1>num3:
    print("num1 is largest")
elif(num2>num3 and num2>num1):
    print("num2 is the largest")
elif(num3>num2 and num3>num1):
    print("num3 is the largest")
elif(num1==num2 and num1==num3):
    print("equal")



#find the second largest number


num1=int(input("num1"))#100
num2=int(input("num2"))#20
num3=int(input("num3"))#15
if (num3>num2 and num2>num1):
    print("num2 is the second largest")
elif(num1>num3 and num2<num1):
    print("num3 is the second largest")
elif(num2>num1 and num3<num1):
    print("num1 is the second largest")


#using elif
n1=20
n2=50
if(n1==n2):
    print("two numbers are equal") #if this "if" is false then it go to next elif statement,elif statement is false then it goes to else statement.
elif(n1>n2):
    print("n1 is greater")
else:
    print("n2 is greater")

#sorting 3 numbers

num1=int(input("num1"))
num2=int(input("num2"))
num3=int(input("num3"))
if(num1>num2 and num1>num3):
    if(num2>num3):
        print("num1,num2,num3")
    else:
        print("num1,num3,num2")
if(num2>num1 and num2>num3):
    if(num1>num3):
        print("num2,num3,num1")
    else:
     if(num3>num1 and num3>num2):
       if(num1>num2):
        print("num3,num2,num2")
     else:
        print("num3,num2,num1")   


#assign:year=leap year

year=int(input("enter the year:"))
if(year % 400==0) and (year % 100 ==0):#if the year is century year we use divide by 400 and for century we divide ny 100
    print(" leap year",year)
elif(year % 4==0) and (year % 100!=0):#if the year is non century year we use divide by 4 and for non century we do not divide by 100
    print(" leap year",year)
else:
    print("not leap year",year)

    

  #calculate the bmi

weight_inkg=float(input("enter the weight in kg:"))
height_incm=float(input("enter the height in meter:"))
height_inm=height_incm/100
bmi=weight_inkg//height_inm**2
print(bmi)

if(bmi<20):
    print("underweight")
elif(bmi<25):
    print("normal weight")  




