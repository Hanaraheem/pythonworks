#sequence of character
#it is a class
#logic= name="hanna"
#double qou
#class inte inside 
    #   methods
name="hana12"
#1.casefold -is inside the str class (covert to uppercase)
print(name.casefold())
#2.capitalize- (only the first letter of the word should be capital)
print(name.capitalize())
#3 . count-it is used for count the specify character (not all the character)
print(name.count("a"))
#4  .index-position of specify character
print(name.index("n"))
#5  .strip-remove either form left or right
print(name.strip("ha"))
#6 .rstrip -if we want to remove form right side
print(name.rstrip("a"))
#7 .lstrip -if we want to remove form left side
print(name.lstrip("h"))
#8.isalpha()- check the string contain only  alphabets (then true oterwise false)
print(name.isalpha())
#9.isdigit()-stirng is full of digit
print(name.isdigit()) 
#10.isalnum-check number and alpha (if space and special chara comes it will gave false)
print(name.isalnum()) 
#11.split- splitting the words
name="python is a programming language"
word=name.split("  ")
for w in word:  #it is used for gave space to one letter on a word
    print(w)
#12.startswith-the word start with specified char
#13.endswith-end with



#print words starting with vowels

name="python is a programming language"
words=name.split(" ")
for word in words:
    if(word[0]=="a" or word[0]=="e" or word[0]=="i" or word[0]=="o" or word[0]=="u"):
     print(word)

     #or

text="python is a programming language"
words=text.split("  ")
vowels=("a","e","i","o","u")
for w in  words:
   if w.casefold().startswith(vowels):
      print(word)

    



tweets="what a game,hats off to both teams.well done @benstokes38 @patcummins30 you have boght test cricket back to life.love test cricket "
words=tweets.split(" ")
for w in words:                     #logic 1.split
                                      #2.for w
                                 #3.if w.startswith
 if w.startswith("@"):
     print(w)