 #rules
#1.first 3 chara must be uppercase random alpha
#2.4rth posi -any one of them(P,C,F,H,T,A)
#3.5th-random uppercase alpha
#4.6th-4digit
#5.10th-one alpha

from re import*
pancard=input("enter pancard number:")
rule="[A-Z]{3}[PCFHTA]{1}[A-Z]{1}[\d]{4}[A-Z]{1}"
matcher=fullmatch(rule,pancard)
print("invlaid" if matcher==None else "valid")


