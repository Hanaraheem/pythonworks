#print all odd numbers within a given range(end) by user
end=int(input("enter the number:"))
i=1
while(i<=end):
    print(i)
    i=i+2


# #another method using while and if
i=2
end=int(input("enter the number:"))
while(i<=end):
    if(i%2!=0):
        print(i)
    i=i+1

 
#even  using while statement and if ;
i=2
end=int(input("enter the number:"))
while(i<=end):
    if(i%2==0):
        print(i)
    i=i+1

#assign:print number  which are divisible by 3,5 and upto given range(starting,end- user given)

# i=int(input("enter the start number:"))#starting
# i1=int(input("enter the end number:"))#ending
# while(i<=i1):
#     if(i%3==0 and i1%5==0):#(we can also use 2 if on this statement)
#         print(i)
#     i=i+1

#prgm to print hi if 9 divisible ,print hello if 18 divisible
i=int(input("enter the  number:"))

while(1<=i):
  if(i%9==0):
    print("hi")
    i=i+1
  elif(i%18==0):
    print("hello")
    i=i+1
    




#sum of natural numbers upto 10
# num=1
# sum=0
# while(num<=10):  #num=1<10,2<=10,......
#     sum=sum+num  #sum=0+1=1,1+2=3.....
#     num=num+1    #num=2,num3
# print("sum of natural number upto 10:",sum)

#sum of odd number range given by user
#sum of even numbers

#odd
# num=int(input("enter the startingnumber:"))
# num2=int(input("enter the endingnumber:"))
# sum=0
# while(num<=num2):
#     if(num%2!=0):
#       num=num+1
#     sum=num+sum
#     print(sum)

    #even

# start=int(input("enter the startingnumber:"))
# end=int(input("enter the endingnumber:"))
# sum=0
# while(start<=end):
#     if(start%2==0):
#       start=start+1
#     sum=start+sum
#     print("sum of all even",sum)



#you are having an arthmetic sequence with a common difference of 6
#the sequence is starting with "56" find the sum of first 10 terms in this sequence

start=56
n=10
d=6
end=start+(n-1) * d
sum=0
# end=104
while(start<=end):
  start=start+1
  sum=(n*(2* start + (n-1)*d)) / 2
print(sum)
print(end)
