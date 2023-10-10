from re import*

text="goodmorning sachin1"
pattern="[aeiou]" #vowels
pattern="[^aeiou\W\d]" #consonents (\W-in this case remove special character)
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())


    
