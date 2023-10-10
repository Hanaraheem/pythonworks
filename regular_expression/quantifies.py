 #python inte rule ulla quantifies

#etrannam undanne nokkan
#+
#*
#(1,2)
#a(12)-a 12 times venam
from re import*
text="aabbaacc"
# pattern="a+"#one or more than one
# pattern="a*"#zero or more occurance(ullatum illatatum print aavum match aavunnate aa positionil matram)
pattern="a{1,2}" #match a mini one time max 2 time
matches=finditer(pattern,text) #finditer is used for searching with each char
for m in matches:
    print(m.start(),m.group())