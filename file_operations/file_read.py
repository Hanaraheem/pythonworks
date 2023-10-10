   # in file,there are 3 operators -read,write,append
#if we want to read :
 #steps:
#1.create data txt file
#2.create file_read.py file
#3.syntax:variable name=open(path of data.txt,r) (open keyword is must)


#if we want to read data.txt: 
#syntax:variable name=open(path of data.txt,mode)
# there are 3 mode-read,write,append
#\\ use for getting output

f=open("C:\\Users\\HP\\Desktop\\luminar_python\\file_operations\data.txt","r") #(2 slash)
# for line in f:
    # print(line)

#into list
words=[line.rstrip("\n")for line in f]
print(words)