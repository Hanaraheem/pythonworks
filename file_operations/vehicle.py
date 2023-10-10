f=open("C:\\Users\\HP\\Desktop\\luminar_python\\file_operations\\numbers.txt")
#print all numbers
all_numbers=[line.rstrip("\n") for line in f]
print(all_numbers)
#print only kerala vehicle numbers
kl_numbers=[num for num in all_numbers if num.startswith("kl")]
print(kl_numbers)

