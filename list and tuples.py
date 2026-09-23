
# #list in Python

marks=[87, 89, 76, 34, 54]
student=["karan", 77,"khan"]
student[0]="arjun"
print(len(student))

mark=[99.4, 87.5, 78.4, 88.2]
print(marks)
print(type(marks))
print(len(marks))
print(mark[0])
print(mark[1])

#list slicing

marks=[99, 87, 77, 34, 25]
print(marks[1:3])
print(marks[ :4])
print(marks[1: ])
print(marks[-3:-1])

 #list methods

list=[3, 1, 2, 4]
print(list.append(5),list)

print(list.sort(), list)
print(list.sort(reverse=True), list)
print(list.reverse)
print(list)
print(list.insert(1,5))


# #list.insert("ammar","khan"))


marks=float(input("Enter your marks:"))
if(marks>=90):
    print("grade:o")
    if(marks>=50):
        print("grade:clear")
    else:
        print("pass")
else:
    print("fail")          

#list insert, remove method

list=[1, 2, 3, 4]
list.insert(0, 5)  # it change and swap the element  
print(list)
print()

#variable swap in python
list=[1, 2, 3, 4]
list.insert(3, 5)
print(list)

# it remove the element from the listlist=[1, 2, 3, 4]
list.remove(3)
print(list)

# pop method remove the last element from the list
list=[1, 2, 3, 4]
list.pop(3)
print(list)

#tuple in python
tup=(1, 2, 3, 4)
print(type(tup)) # output = tuple

tup= (87, 98, 57, 62, 23)
print(tup[0])
print(tup[1])
print(tup[2])

tup=()
print(type(tup)) 
print(tup)

tup=(1)  #-> this is not a tuple if we want to make it a tuple we have to add a comma after the element
print(type(tup)) #
print(tup)

tup=(1,)  #-> this is a tuple
print(type(tup)) 
print(tup)


 #slicing in tuple
tup=(1, 2, 3, 4, 5)
print(tup[1:3])

# tuple methods
tup=(1, 2, 3, 4, 5,5,5)
print(tup.count(5))
print(tup.index(5))

# wap to ask the user to enter names of their fav movies and store them in a list and print the list
movie=[]
mov1=str(input("Enter your 1st fav movie:"))
mov2=str(input("Enter your 2nd fav movie:"))
mov3=str(input("Enter your 3rd fav movie:"))
movie.append(mov1)
movie.append(mov2)
movie.append(mov3)
print(movie)

#method 2
movie=[]
mov1=str(input("Enter your 1st fav movie:"))
movie.append(mov1)
mov2=str(input("Enter your 2nd fav movie:"))
movie.append(mov2)
mov3=str(input("Enter your 3rd fav movie:"))
movie.append(mov3)
print(movie)

movie=[]
for i in range(3):
    mov=str(input("Enter your fav movie:"))
    movie.append(mov)

print(movie)


list1=[1, 2, 1]
list2=[1, 2, 3]
copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("number is palindrome")
else:
    print("number is not palindrome")
