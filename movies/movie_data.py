from json import load
path="C:\\Users\\HP\\Desktop\\luminar_python\\movies\\mdb.json"
with open(path,encoding="UTF-8") as f:
    filims=load(f)

#print total number of filims
print(len(filims))

#print all movie names in 2015
movie_filters=[f.get("title")for f in filims if f.get("year")=="2015"]
print(movie_filters)

#print crime movies
comedy_movie=[f.get("title")for f in filims if "Comedy" in f.get("genres")]
print(comedy_movie)

#id=range(20,30) and runtime>150

movies=[f.get("title")for f in filims if f.get("id") in range (20,30) and f.get("runtime")>="150"]
print(movies)

#print one word filims
movies_oneword=[f.get("title")for f in filims if len(f.get("title").split(" "))==1]
print(movies_oneword)

#print highest runtime in drama genres

drama=[f for f in filims if "Drama" in f.get("genres")]
max_runtime=max(drama,key=lambda f:int(f.get("runtime"))) #int is used for finding max runtime
print(max_runtime)

#print all genres (without repetation)
genres={f.get("genres")for f in filims } #to remove repeatation we use{}
print(genres)



#print which year is most filims relesesed
wc=[]
for f in filims:
    year=f.get("year")
    if year in wc:
        wc[year]+=1
    else:
        wc[year]=1
# out=max(wc,key=lambda k:wc.get(k)) -wc.get
# print(out)
    #or
print(max((v,k)for k,v in wc.items())) #in  this prgm we gave value first and then key
                                       #eg:10-2020






