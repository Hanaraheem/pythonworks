                 #lambda_function
#it is used for minimise the program lenght
#in this we use lambda keyword instead of def and also return on same line
  #syntax: a=lambda variable: return statment condition(if present)
#square
square=lambda n1:n1**2
print(square(4))
#cube
cube=lambda n1:n1**3
print(cube(4))
#max
max_two=lambda n1,n2:n1 if n1>n2 else n2
print(max_two(4,3))
#min
min_two=lambda n1,n2:n1 if n1<n2 else n2
print(min_two(4,6))


#find the longest word
txt="hi hello hai goodafternoon python"
words=txt.split(" ")
max_word=max(words,key=lambda w:len(w)) #key is used for print the word with lenght of highest word
print(max_word)                         #if we do not gave key, the max_word is hello

#sorted in descen
srt=sorted(words,reverse=True,key=lambda w:len(w))
print(srt)