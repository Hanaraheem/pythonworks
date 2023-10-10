#1*2=2.....10*2=20
#multiplication table

num=1
while(num<=10):
    print(f"{num} *2={num*2}")
    num=num+1
    

#factorial
#4!=1*2*3*4
num=4
start=1
f=1
while(start<=num):
    f=f*start
    start=start+1
    print(f)

#digit #234(only stop till zero )
 #output =
 # 4
 # 2
 # 3

 
 # num=234
 # digit=num%10
 # >> 4 remin,num=234
 #num//10 floor using for remove point value 
 # >>num=23 
 # digit=num%10
 # >>digit
 # 3  
 # >>num=num//10
 # >>num
 # >>>digit=num%10
 # >>>digit
 # 2
 # >>num=num//10
 # num=0   


num=324
while(num!=0):
    digit=num % 10
    print(digit)
    num=num//10




print("3",end="")#if we want to print 34 in one line we use "end=""
print("4")
                  #or
# str=""
# str+=str(value)
#print(str)
num=324
stri=""
while(num!=0):
    digit=num % 10
    stri+=str(digit) #str=""+4="4"  "4"+"2"="42"  "42"+"3"=423
    num=num//10#answer come in one line not one by one
print(stri)


#sum of digit
#num=324
#4+2+3=9

num=324
sum=0
while(num!=0):
    digit=num % 10
    sum=sum+digit
    num=num//10
print(sum)

#product of digit
#3*2*5

num=324
product=1
while(num!=0):
    digit=num % 10
    product=product*digit
    num=num//10
print(product)

#cube sum of digit
#1**3+2**3+3**3
num=324
sum=0
while(num!=0):
    digit=num % 10
    cube=digit**3
    sum=cube+sum
    num=num//10
print(sum)






