#for loop

#inside the class it is called method otherwise function.
#\n is used to print on next line(line by line)
#for i in range(start,stop,step), start=starting value,stop=ending value (if 10 range 9 vere print),step=increment or dicre(jump)

# #print 1 to 10
for i in range(1,11,1):
    print(i)
#print 10 to 1
for i in range(11,1,-1):
    print(i)


#user input
low_limit=int(input("enter the low limit:"))
upper_limit=int(input("enter the upper limit:"))
for i in range(low_limit,upper_limit):
    print(i)


#print all even numbers b/w lowerlimit and upperlimit

# low_limit=int(input("enter the low limit:"))
# upper_limit=int(input("enter the upper limit:"))
# for i in range(low_limit,upper_limit):
#     if(i%2==0):
#         print(i)



#divisibe by3=fizz,5-buzz,15-fizz buzz ,not divisible print that number

low_limit=int(input("enter the low limit:"))
upper_limit=int(input("enter the upper limit:"))
for i in range(low_limit,upper_limit):
    if(i%3==0):
        print("fizz")
    if(i%5==0):
        print("buzz")
    if(i%15==0):
        print("fizz buzz")
    if(i%3 or i%5 or i%15 !=0):
        print(i)
    
# factorial 
 
num=int(input("enter the number:"))
fac=1
for i in range(1, num+1, 1):
  fac=fac*i
  print(fac)

#hcf- higest common factor ( 2 number ne divide cheyyan patiya largest common factor)     
# num1=18
# num2=9  #1,3,9-this are the common factor and the largest is 9 in 10 range so it is hcf
# logic=num1 %i==0 and num2 %i==0
# hcf=i


num1=18
num2=9  #(num2 is always smaller than num1)
for i in range(1,num2+1):#from left side
    if num1 %i==0 and num2 %i==0:
        hcf=i
print(hcf)




#vowels print
#ch -one by one character print

text="coffee"
for ch in text:
    if ch in ["a","e","i","o","u"]:
      print(ch)

#count of vowels and consonent

text="ettayi coffee"
v_count=0
c_count=0
for ch in text:
    if ch in ["a","e","i","o","u"]:
       v_count+=1
    else:
        c_count+=1
print("vowel count",v_count)
print("consanant count",c_count)

