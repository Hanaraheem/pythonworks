from re import*
phno_rule="\d{10}"
mail_rule="[a-z][\w\W]+[@](gmail)[.]com"
mail_id=[]
phno=[]


f=open("C:\\Users\\HP\\OneDrive\\Desktop\\luminar_python\\regular_expression\\data.txt","r") 
for line in f:
    words=line.rstrip("\n").split(" ")
    for w in words:
        p_matcher=fullmatch(phno_rule,w)
        e_matcher=fullmatch(mail_rule,w)
        if p_matcher!=None:
            phno.append(w)
        elif e_matcher!=None:
            mail_id.append(w)
print(phno)
print(mail_id)