arr=[10,20,30,20,"hello",True] #location 0=10 ,1=2 ,2=30
print(arr[0]) #only 10 print
print(arr)#print all

arr[1]=200 #updatation arr[position]= new value
print(arr)


expenses=[10000,12000,23000,12000,25000,14000]
 #          0      1     2    3      4    5
print(expenses[0]) # exp of jan month

for e in expenses:
    print(e)          #print all expense


total=0
for e in expenses:        #total expense(sum of exp)
    total+=e
print(total)



#list programs
filims=["vigathakumaran","marthandavarma","balan","nirmala"]
#print(filims)
for f in filims:
    print(f)




#progam
expenses=[12000,13000,14000,1100,25000,28000,21000]
#print march month from expenses
print(expenses[2])
#print all expenses
for e in expenses:
    print(e)  
#print costly expense 
max_exp=0
for e in expenses:
    if e>max_exp:
     max_exp=e
print(max_exp)   
#print expenses>16000
for e in expenses:
    if e>16000:
     
      print(e)   

#program to find min of  expen
min_exp=expenses[0]
for e in expenses:
    if e<min_exp:
     min_exp=e
     
     print(min_exp)

#print total,minimum,maximum using sum,min,max functions
total_exp=sum(expenses)
print(total_exp)
min_exp=min(expenses)
print(min_exp)
max_exp=max(expenses)
print(max_exp)

#sorting-sort function is used
srt_exp=sorted(expenses,reverse=False) #print acend
srt_exp=sorted(expenses,reverse=True)#print decen


#list methods
#1.append()-element add into the list(at the end)
users=["mohanlal","mammotty","nivin","dq","nivin"]
users.append("sreenivasan")
print(users)
#2.pop-remove element from the list.
users.pop(3)
print(users)
#3.index()- index position
print(users.index("nivin"))
#4.count-how many times that objt occurance
print(users.count("nivin"))
#5.sort-for sorting
users.sort()
print(users)
#6.clear-for clearing the elements
users.clear()
print(users)
#in()-(membership operator)-used for find the searching element is present or not.
users=["mohanlal","mammotty","nivin","dq","nivin"]
if ("sreenivasan"in users):
   print("present")

else:
   print("not")

#not in()- not in the list
users=["mohanlal","mammotty","nivin","dq","nivin"]
if ("sreenivasan"not in users):
   print("valid")

else:
   print("invalid")

#prblm add lee_frnds into kdrama
kdrama=["lee jong",
        "seo",
        "gong yoo",
        "heyn"]
lee_frnds=["seo","gong yoo","heyn"]
for p in kdrama:
   if p not in lee_frnds:
      print(p)

 #2nd recrussive character using 2 lists

text="abaccabb"
dupli_text=[] #first list
nondupli_text=[] #2nd list
for ch in text:
    if ch in dupli_text:
       dupli_text.append(ch) 
    else:
        nondupli_text.append(ch)
print(dupli_text[1])

  #kangaroo word (using list)
source_word="chicken"
target_word="hen" #output
source_word_list=[] #list1
kangaroo_string=""
for ch in source_word:
        source_word_list.append(ch) #if the ch is in source_word add to source_word_list
for ch in target_word:
    if ch in source_word_list:#if the ch in present in target,it also present in source_word_list 
        source_word_list.pop(source_word_list.index(ch)) #remove the ch from sour and
        kangaroo_string+=ch #add  ch into kangaroo
print(kangaroo_string==target_word)         

