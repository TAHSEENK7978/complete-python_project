# f=open("demo.txt", "r")

# data = f.read()
# print(data)

# line1=f.readline()
# print(line1)

# line2=f.readline()
# print(line2)
# print(type(line2))

# f.close()

#w
# = write over the file means delete and add new txt, "a"= add new txt or append
f=open("demo.txt", "w","a")
f.write("My name is tahseen khan")
f.write("i'm from jharkhand")
f.close()