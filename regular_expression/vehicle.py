 #Rules
#1.KL
#2.2 digits
#3.1 min or max 2 apha
#4.4 digits

from re import*
vehicle_no=input("enter the number:")
rule="KL-[\d]{2}-[A-Z]{1,2}-[\d]{4}"
matcher=fullmatch(rule,vehicle_no)
print("invalid" if matcher==None else "valid")
