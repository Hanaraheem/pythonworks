#break ,continue keyword
#mainly using is break
#break is used to stop(loop inte outside ilakke)
#continue-skip that portion (loop il tanne tiriche varum  )

# num1=18
# num2=9  #(num2 is always smaller than num1)
# for i in range(1,num1,-1):#from right side
#     if num1 %i==0 and num2 %i==0:
#         hcf=i
#         break
# print(hcf)


#break

# for i in range(1,51):
#     if i==25:
#         break  
#     print(i)

#continue
# for i in range(1,51):
#     if i==25:
#         continue  
#     print(i)


#prime number
#1,7,11,13...
#in prime number only 2 factors  
#eg: 7- 1,7(not other number divisible) so we check from 2-6 loop 
#11- 1,11
#logic: is_prime=true ,for i in range(2,num):,if num %i==0 (1,7 only true,others false)then prove that is prime


# num=int(input("enter the number"))
# is_prime=True
# for i in range(2,num):
#     if num %i==0:
#         is_prime=False
#         break
# print(is_prime)



#assignment

#1. sum of all numbers from 1 to 10 using for loop
#2. multiplcation table
#3.factorial
#4.fibonacci series


#1.sum of number

n=1
sum=0
for i in range(1,10):
    sum=sum+i
    print(sum)


#2.multiplication
n=int(input("enter the number:"))
for i in  range(1,11):
    print(f"{n} *i={n*i}")
    


#factorial

n=int(input("enter the number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
    print(fact)


#fibonocci series

prev=0
current=1
print(prev)
print(current)
start=1
for i in range(1,n+1):
    fib=prev+current
    print (fib)
    prev=current
    current=fib
    start=start+1


