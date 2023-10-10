#program to find voting eligiblity using if else

age=int(input("enter your age:"))
if(age>=18):
     print("eligilible for voting")
else:
     print("not eligilible for voting")


#find fever of a person

cels=float(input("enter your fever temperature:"))
fahr=cels*(9/5)+32
print(fahr)
if(fahr>99):
    print("the person is sick")
else:
    print("normal temp")

    
#greater and lesserthan, equality 

a=10
b=10
if a>b:
    print("largest number =",a)
if(a<b):
     print("largest number =",b)
if(a==b):
     print("equality =",a==b)
else:
     print("invalid")


#     #largest of 3 number

print("enter the 3 numbers")
num1=int(input())
num2=int(input())
num3=int(input())
if (num1>num2): 
    if (num2>num3):
       largest=num1
    else:
     if(num3>num1):
      largest=num3
     else:
      largest=num1
if(num2>num3):
     largest=num2
else:
     largest =num3
print("largest number is=",largest)



#using by if only grading system

mrk=int(input("enter the mark:"))
if(mrk>=90):
    print("A+")
if(mrk<90 and mrk>=80):
    print("A")
if(mrk<80 and mrk>=70):
    print("B+")
if(mrk<70 and mrk>=60):
    print("B")
if(mrk<60 and mrk>=50):            
    print("C+")
if(mrk<50 and mrk>=40):
    print("C")
if(mrk<30):
    print("D+")
else:
    print("failed")





#program to find the first alphabet of a word is an vowel or not

word=input("enter the word:").casefold() #(it is used for convert into capital letters into lover case)
if(word[0]=="a" or word[0]=="e" or word[0]=="i" or word[0]=="o" or word[0]=="u"):
    print("vowel")
else:
    print("consonant")


    

