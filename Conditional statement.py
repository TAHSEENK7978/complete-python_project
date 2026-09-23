
#age limit

age=input("Enter you age:")

if(age >=" 18"):
    print("can vote  can drive")
else:
    print("not eligible")


#marking system
marks=input("Enter the marks of the student:")

if(marks >= "90"):
    grade="A"

elif(marks >= "80" and marks < "90"):
    grade="B"

elif(marks >= "70" and marks < "80"):
    grade="C"

elif(marks >= "60" and marks < "70"):
    grade="D"
elif(marks >= "50" and marks < "50"):
    grade="E"
else:
    grade="fail"

    print("grade of the student is ->", grade)

#no is divisible by 3


num=int(input("Enter the number:"))

if(num % 2 == 0):
    print("even number")
else:
    print("odd number")

#largest 3 numbers

a=int(input("Enter 1st no:"))
b=int(input("Enter 2nd no:"))
c=int(input("Enter 3rd no:"))

if(a > b and a > c):
  print("a is the largest number")
elif(b > a and b > c):
  print(" b is the largest number")
else:
  print("c is thelargest number")

#no is divisible by 7 or not

num=int(input("Enter the number"))

if(num % 7 ==0):
    print("number is divisible by 7")
else:
        print("number is divisible by 7")

#greatesst of 4 number
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
d=int(input("Enter 4th number:"))

if(a>b and a>c and a>d):
    print("a is the largest number", a)
elif(b>a and b>c and b>d):
    print("b is the largest number", b)
elif(c>a and c> b and c>d):
    print("c is the largest number", c)
else:
    print("d is the largest number", d)





          