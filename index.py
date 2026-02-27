print('hello world')
name="Mary"
print(name)
name=input("enter your name:")
print("Hello" , name)
p="Phill"
age=23
city="Nairobi"
print(p,"is ",age,"and lives at", city)
price=float(input("enter price:"))
#assinin variables the same value
a=b=c=20
print(a,b,c)
#assinin different variables different values
x,y,z=10,20,"Mary"
print(x,y,z)

#Type Casting a Variable
s="10"
n=int(s)

cnt=5
f=float(cnt)

age=23
s2=str(age)
print(n)
print(cnt)
print(f)

# Swapping Two Variables
a, b = 5, 10
a, b = b, a
print(a, b)

#Counting Characters in a String
word = "Python"
length = len(word)
print("Length of the word:", length)

#python operators
#_______Arithmetic operators(example +,-,*,/,%,**,//)
# Variables
a = 15
b = 4

# Addition(+)
print("Addition:", a + b)

# Subtraction(-)
print("Subtraction:", a - b)

# Multiplication(*)
print("Multiplication:", a * b)

# Division(/)
print("Division:", a / b)

# Floor Division(//)
print("Floor Division:", a // b)

# Modulus(%)
print("Modulus:", a % b)

# Exponentiation(**)
print("Exponentiation:", a ** b)
a = True
b = False
print(a and b)    #output is False
print(a or b)     #output is True
print(not a)      #outputs False

x=10
y=12
c=-10
if x>0 and y>0:      #outputs both numbers are positive
    print ("Both numbers are greater than 0")
else:
    print ("Both numbers are less than 0")
if x>0 and y>0 and c>0:   #outputs At least one of the numbers is less than 0
    print ("all the numbers are greater than 0")
else:
    print("At least one of the numbers is less than 0")


#Logical operators (AND,OR,NOT
m=23
n=-12
q=0
if m>0 or n>0:         #output Either of the numbers is greater than 0
    print("Either of the numbers is greater than 0")
else:
    print("No number is greater than 0")
if m>0 or n>0 or q>0:   #Either of the numbers is greater th
    print("Either of the numbers is greater than 0")
else:
    print("No number is greater than 0")