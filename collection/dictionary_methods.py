               #METHODS

#1.keys-it is used for displaying keys 
student={"name":"kaavu","age":21,"course":"python"}
for k in student.keys():
    print(k)
#2.values-to return values from dictionary
for v in student.values():
    print(v)
#3.items-print both key and values(mainly used)
for k,v in student.items():
    print(k,v)
#4.get-fetch value from key
#print(student["names"])(if key is not in the dict,it will provide error mess)
print(student.get("name")) #(not error mess)
#5.pop-it is used to remove key value
student.pop("age")
print(student)


#program to find non recrussive characters
text="abcaabbde"
wc={}
for ch in text:
    if ch in wc:   #count of the character
         wc[ch]+=1
    else:
        wc[ch]=1

for k,v in wc.items(): #take the key and values using method .items()
    if v==1: #if value==1,print key
        print(k)

        # or
        text="abcaabbde"
wc={}
for ch in text:
    if ch in wc:   #count of the character
         wc[ch]+=1
    else:
        wc[ch]=1
        print(ch)
        break

#program to find second recrussive character

text="abaccabb"
wc={} #empty set for dict
duplicate_list=[]  #empty set for list
for ch in text:
    if ch in wc: 
       duplicate_list.append(ch) #if the ch duplicate present in wc it covert into list
    else:
        wc[ch]=1
print(duplicate_list[1])#position 1 in the list is the second recurrise,so print it

#kangaroo (dict  is easy than list)
#check thetarget word with dicti(sourse code)count<0,element undonnum then decrement the count by target count
 #source_word=decreases                        #   dict        compare target with source if it is then drement by the numner of targ
 #target_word=dress                  #   d                1     1-1=0
                                     #   e                2
                                     #   c                1
                                     #   r                0
                                     #   a                1
                                     #   s                2    2-2=0


source_word="decreases"
target_word="dress"

wc={}
for ch in source_word:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1
for ch in target_word:
    if ch in wc and wc.get(ch)>0:
        wc[ch]-=1
    else:
        print("not kangaroo word")
        break



