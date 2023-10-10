#rule
#1.3digits
#2./
#3.2digits
#4.R
#5.2digit
#6./
#7.2digitwith one aplha

from re import*
code=input("enter the code:")
rule="[\d]{3}[/][\d]{2}[R][\d]{2}[/][\d]{2}[A-Z]"
matcher=fullmatch(rule,code)
print("invalid" if matcher==None else "valid")