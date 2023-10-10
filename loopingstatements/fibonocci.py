#fibonocci series
#0 ,0+1 ,0+1+2, 
# prev=0
# curr=1 
# print prev and curr
#( while) end=9,start=1
# fib=pre+cur
# print fib
# prev=curr
# curr=fib


prev=0
current=1
print(prev)
print(current)
start=1
while(start<=9):
    fib=prev+current
    print (fib)
    prev=current
    current=fib
    start=start+1

#cube sum of digit eg:121
#1**3+2**3+3**3


#sum=0
#while
#cube=d**3
#sum=sum+cube
#floor division


num=int(input("enter the value"))
sum=0
while(num!=0):
    digit=num % 10
    cube=digit**3
    sum=sum+cube
    num=num//10
print(sum)




#ambstrong number:(cube sum value =original number )eg:153
#sum==num(logic)  same value as output

num=int(input("enter the value"))
sum=0
original=num
while(num!=0):
    digit=num % 10
    cube=digit**3
    sum=sum+cube

    num=num//10
print(sum)
if(sum==original):
    print("number is ambstrong")
else:
    print("not ambstrong")


