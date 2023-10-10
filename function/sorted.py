#it is an function
#it is used for sorting
#it used in both digit and charac




#sorting using sorted function

text="cabbage"
srt_word=sorted(text)
print(srt_word)

#check anagram or not

#anagram-it is used to know the text alphabets is same as out alphabet
text="race"
out="care"
if sorted(text)==sorted(out):
    print("anagram")
else:
    print("not anagram")

#1.palindrome
#text="malayalam"

text="malayalam"
if(text==text[::-1]):
       print("palindrome")
else:
     print("not palindrome")

    #or
text="malayalam"
count=len(text)-1
p_str=""
for i in range(count,-1,-1):
     p_str+=text[i]
print("palindrome" if text==p_str else "not palindrome")
    
