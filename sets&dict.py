#dictonary is a build-in datatype is used to store data in key-value parts . it 
#is unoderable , mutable and don't allow duplicate value 

info = {
    "name":"tahseen",
    "class":"3rd sem",
    "roll_no":"100",
}
print(info)

stud = {
    "name":("sami", "tabish", "talish", "ali"),
    "age": (23, 22, 21, 19), 
    "marks":(87, 98, 76, 82),
}
print(stud.get("name")[1])
print(stud.get("age")[1])
print(stud.get("marks")[1])

for key,value in stud.items():
    print(key, "->", value)

