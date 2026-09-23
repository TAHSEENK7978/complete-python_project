
#print hello world 5 times

count=1
while count<=5:
    print("hello world")
    count+=1

#printing numbers 1  to 100 

i=1
while i<=100:
    print(i)
    i+=1

#printing one to lakh 

i=1
while i<=100000:
    print(i)
    i+=1

#print infinity numbers /infinite loops are very dangerous it crash the browser

i=1
while i>=1:
    print(i)
    i+=1

#printing reverse numbers in while loop from lakh to 1
 
i=100000
while i>=1:
    print(i)
    i-=1
    print("loop ended")


#printing a multiplication table of "n" numbers

n=int(input("Enter the number:"))
i=1
while i>=1:
    print(n*i)
    i+=1

# even odd in short 
a=int(input("Enter the number"))
print("even" if a%2==0 else "odd")

# to check the number is palandrome or not

#print the number the following
[1, 4,9,16,25,36,49,64,81,100]

#print these number by using while loop

nums=[1, 4, 9, 16, 36, 49, 64, 81, 100]
idx=0
while idx < len(nums):
    print(nums[idx])
    idx+=1

#search for a number x in this tuple using the loop
num=[1, 2, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x=2
i=0
while i<len(num):
    if (num[i]==x):
        print("found at index:", i)
    
        i+=1
        
num=[1, 2, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x=4
i=0
while i < len(num):
    if(num[i]==x):
        print("found at index:", i)
        i+=1

i=1
while i<=1:
    print(i)
    i-=1
    
i=1
while i< 10:
    print(i)
    if (i ==3):
        break
    i+=1
   
#finding the specific number in the list using while loop

nums=[1,4, 9,16,25,36,49,64,81,100]
x=36
i=1
while i < len(nums):
    if(nums[i]==x):
        print("found at index:", i)
        break
    else:
        print("finding....")
        i+=1
        print("End of the loop")

#skipping the specific number in the list using while loop
i=2
while i <= 5:
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1

#even odd number using while loop
i=0
while i<=20:
    if(i%2==1):
        i+=1
        continue
    print(i)
    i+=1
i=1
while i<=10:
    if(i % 2 ==0):
        i+=1
        continue
        print(i)
        i+=1

# for loop
nums=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for val in nums:
    print(val)


tup=["a", "b", "c", "d"]
for val in tup:
    print(val)

#
names=("tashseen", "sahil", "talib", "akmal")
for val in names:
    print(val)

#
tup=[1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in tup:
    print(num)


str="thaseen khan"

for char in str:
    if(char=='e'):
        print("e found")
        break
    print(char)
else:
    print("end")

#print this numbers using the loops

num=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for el in num:
    print(el)

num=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 16]  #this is called linear search
x=16
idx=0

for el in num:
    if(el == x):
        print("number found at idx:", idx)
    idx+=1

#range function
for i in range(5):          #range(stop)
    print(i)

#
for i in range(1,5):        #range(start, stop)
    print(i)

for el in range(1,5,2):     #range(start, stop , step)
    print(el)

#even
for i in range(2,100,2):
    print(i)

#odd
for i in range(1,100,2):
    print(i)

#print no from  1 to 100
for i in range(1,100):
    print(i)

#print no from 100  to 1
for i in range(100,0,-1):
    print(i)

n=int(input("enter the number:"))
for  i in range(1,11):
    print(i * n)

#factorial of "n" numbers for loop
n=10
fact = 1
for i in range(1, n+1):
    fact*=i
    print("total factorial:", fact)

#factorial of "n" no's for while loop

n=10
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
    print("fact of no's:", fact)


#skip a particular number
i=0
for i in range(0,10): 
    if(i==4):
        continue
    i+=1
    print(i)

#sum of the numbers
num=[2, 4, 6, 8]
total=0
for num in num:
    total+=num
    print("SUM IF THESE NUMBERS:", total)

