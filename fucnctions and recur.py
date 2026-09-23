#Function defination
def calc_sum(a,b):      ##parameters(a,b)
    sum=a+b
    print(sum)
    return sum
calc_sum(5,10)          #Function call ; Argument
calc_sum(5,10)       
calc_sum(7,8)

def calc_sum(a,b):
    return a+b

sum=calc_sum(1,3)
print(sum)

#multiple lines txt
def print_hello():
    print("hello")
print_hello()
print_hello()
print_hello()                                  #there are two types of functions
print_hello()                                  #1.built-in fuction      
print_hello()                                  #2.user defined function

#Avg of 3 numbers
def cal_avg(a,b,c):                                         
    sum=a + b + c
    avg=sum/3
    print(avg)
    return avg
cal_avg(4,5,6)

#ex of user defined function
#1.
def cal_prod(a=4, b=2):
    print(a*b)
    return a*b
cal_prod()
#2.
def calc_prod(a, b=6):
    print(a*b)
    return a*b
calc_prod(4)

#3.
def calc_prod(b, a=5):
    print(a*b)
    return a*b
calc_prod(8)

#wap to print the lenth of the list
num=[1, 2, 3, 4]
names=["tahseen", "ali", "akmal", "ammar", "aditya", "sami", "maaz"]
def print_len(list):
    print(len(list))

print_len(num)
print_len(names)

#wap to print all the names or str in one line
names=["tahseen", "ali", "tabish", "sami", "akmal"]

def print_len(list):
    for items in list:
        print(items, end=" ")

print(names)

#n numbers of factorial
def calc_fact(n):
    fact=1
    for i in range(1, n+1):
        fact *=i
        print(fact)
calc_fact(5)

#f to convert the usd into inr
def converter(usd_val):
    inr_val=usd_val*96.17
    print(usd_val, "usd", inr_val, "inr")

converter(100)


#Recurision function
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)

def fact(n):
    if(n==1 or n==0):
        return 1
    return fact (n-1) * n
  
print(fact(5))

#printing the sum of n natural numbers
def cal_sum(n):
     if(n == 0):
        return 0 
 
     return cal_sum(n-1) + n

sum= cal_sum(10)
print(sum)

#by using the recursion function to print all the elements in the list 
def print_list(list, idx=0):
    if(idx==len(list)):
        return
    print(list [idx] )
    print_list(list, idx+1)

names=["tahseen", "ali", "tabish", "sami", "akmal"]


print_list(names)