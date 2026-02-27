name=input("Enter your name:")
age=input("Enter your age:")
age=int(age)
city=input("Enter your city:")
print(name,"is",age,"and lives at",city)

#input multiple variables at the same time
# The split() method always returns input values as strings. If you need them as numbers (int or float),
# you must convert them using typecasting.
x, y, z = int(input("Enter three values:")).split()
print("Number of students:",x)
print("Number of girls :", y)
print("Number of boys :", z)


