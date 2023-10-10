#fullmatch=it used for find the exact match
#if no match then print none

from re import*
phone_no=input("enter the number:")
rule="\d{10}" #instead of pattern we use rule
matcher=fullmatch(rule,phone_no)
if matcher==None:
    print("invalid")
else:
    print("valid")
