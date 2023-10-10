      #1.python variable rule

# from re import*
# variable=input("enter the variable")
# rule="[a-zA-Z][0-9a-zA-Z_]"
# matcher=fullmatch(rule,variable)
# print("invalid" if matcher==None else "valid")



            #2.our variable rule
#first alpha must be k--m
#2nd pos digit with divisible by 3
#any number of char

from re import*
variable=input("enter variable name")
rule="[k-m][369][\w]*" #*-character kodukkukayoo ,illatayum erikkam,allel nirbandam aayum kodukkanm
matcher=fullmatch(rule,variable)
print("invalid" if matcher == None else "valid")

          