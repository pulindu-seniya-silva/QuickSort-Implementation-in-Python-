print(12.5)
#comment


#variable types
int 
float
str
bool

a = 10
b = "ABC"

s1 = "Hello"
s2 = 'Hello'
s3='''Hello'''

print(type(s1))

print(type(s2))

print(type(s3))

a = True
print(type(a)) 

#type casting
num = "10"
print(type(num))

num = int(num)
print(type(num))

print(2**3) 

a = 7 % 3
print(a)

a = a + 5
a += 5

n1 = 10
n2 = 20
if (n1 == 10 and n2 == 20):
    print("OK")

#Data structures - 2 parts
#1. Built in Data structures -> List, tuple, set, Dictionary
#2. User Define Data Structures

#List
nums = [10, "Hello", 30.5, 40]
print(nums)

print(nums[2])
print(nums[-1])

nums.insert(1, 'Sri lanka')
print(nums)
nums.remove("Sri lanka")
print(nums)

nums.pop()
print(nums)

print(type(nums))

#Tuple
nums = (2, 3.5, 4, 7)
nums = 10, "Hello", True
print(nums)

print(type(nums))

set = {10, 10.5, "Hello", 10}
print(set)

set.add(11)
set.remove(10)

print(set)

#Dictionary
D1 = {"value 1": "Pulindu",
      "age" : 25,
      "isMarryed" : False,
      }
print(D1["value 1"])

n = 10

if(n < 20) :
    print("ok")
elif n == 10:
    print("no")
else:
    print("Big")


#iteration 
#1 -> for loop
#2 -> while

n = 1

while n < 10 :
    print("Hello !")
    n += 1 # n = n + 1
    if(n == 5):
        continue
else:
    print("Done")

#for loop
print("New Type")
for i in range(10):
    print("ABC")

print("New Type")
for i in range(0, 11, 2):
    print(i)

print("New Type")
for i in range(11):
    print(i)

L = [10, 20, 30, 40]



for x in L:
    print(x)

print(len(L))

for i in range(len(L)):
    print(L[i])

#functions

def sum(n1, n2):
    total = n1 + n2
    return total
print("Sum is")
print(sum(10, 12))

def printName(name):
    return "Full name is " + name

result = printName("Pulindu Seniya")
print(result)

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    
print(factorial(4))

