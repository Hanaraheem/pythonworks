#dcvb#@gmail.com

from re import*
mail=input("enter the gmail")
rule="[a-z0-9][\W\w]+[@]gmail[.]com"
matcher=fullmatch(rule,mail)
print("invalid" if matcher==None else "valid")





