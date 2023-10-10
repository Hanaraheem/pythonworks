#logical operation

#AND(&)-if 2 input gives true then  true ,oterwise false

#OR-if any one input true then the output is true

#NOT-if x is true then the output is false




#     X            Y          AND            OR                NOT
#    True       True          T              T                 F
#    True       False         F              T                 F
#    False      True          F              T                 T
#    False      False         F              F                 T
    



#example

db_username="some username"
db_password="some password"
usernames="your username"
pwd="your pwd"

data=(db_username==usernames)and(db_password==pwd)
print(data)


#(n1>n2)and(n1>n3)
n1=10
n2=20
n3=40
N1=(n1>n2)and(n1>n3)
print(N1)





#BITWISE OPERATOR

#bitwise(and) &, or| ,^(xor), ~(not)
#AND
#0 0=>0
#0 1=>0          0001=1
#1 0=>0          0010=2
#1 1=>1          0011=3

#1 & 2=>0001 & 0010=>0000=0

# 1 | 2=>0001 | 0010=>0011=3
print(1&2)
print(1|2)
#NOT
#for not if the value is positive ,then add one and output in negative sign
#if the value is negative,then sub one and output in positive sign
print("bitwise  not  :",~1)
print("bitwise  not  :",~2)
print("bitwise  not  :",~5)
print("bitwise  not  :",~-3)
print("bitwise  not  :",~-1)
print("bitwise  not  :",~-5)






