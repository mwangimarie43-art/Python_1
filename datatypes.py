#integer
age=23
print(age)
n=int(input("enter no of students:"))
print(n)
price=float(input("enter price:"))
print(price)
total=price*n
print("The total is",total)

# find the data type of input in python
a="Hello world" #int
b=10                         #int
c=2.4
d=("Geeks", "for ","Geeks")  #tuple
e=["Geeks", "for ","Geeks"]  #Array
f={"Geeks", "for ","Geeks"}  #set
g={"Geeks": 1, "for":2}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))