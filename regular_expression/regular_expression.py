#re python
#pattern matching
#eg:email,website,upi,pancard,numberplate
#www,@gmail

from re import*

text="abbababb"
#     012345678
pattern="ab" #searching pattern
matcher=finditer(pattern,text)#variable name=objt(searching pattern,search from where)
for m in matcher:
    print(m.start(),m.group()) #(start(),group())


text="Python 4 567"
#     012345678
# pattern="[a-z]" 
# pattern="[A-Z]" 
# pattern="[a-zA-Z]"
# pattern="[0-9]"  
# pattern="[a-zA-Z0-9]"
# pattern="[^a-z]"#except a-z.
# pattern="\d" #used for take digits
# pattern="\D" #except digits
# pattern="\w"#all characters including digits,spec
pattern="\W"#excpt all character
matcher=finditer(pattern,text)#variable name=objt(searching pattern,search from where)
for m in matcher:
    print(m.start(),m.group())