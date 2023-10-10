        #JSON
#javascript object notation
#it is used for exchanging data's between 2 application
#eg:java->json->python (2 application ile language ne json ilakki aghottum eghottum kodukkum)
#by using json we can convert java into python
#.json exctention
#no need of variable name in json



from json import load #for loading
path="C:\\Users\\HP\\Desktop\\luminar_python\\read_json\\data.json"
with open(path) as f:  #by using this syntax we do not nee closing tag
    record=load(f)
    
#name from records(data.json)

fw_names=[f.get("name") for f in record]
print(fw_names)
 #max rating
max_fw=max(record,key=lambda d:d.get("rating"))
print(max_fw)
           

#print python frame works
py_frame=[f.get("name") for f in record if f.get("language")=="python"]
print(py_frame)

#backend frameworks
bk_frame=[f.get("name") for f in record if f.get("side")=="backend"]
print(bk_frame)




