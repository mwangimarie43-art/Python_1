#For Loop
i=6
for i in range(3,6):
    print (i)


#while loop
a=1
while a<=7:
    print(a)
    if a==3:
        break  #This will exit the loop when a is equal to 3
    a+=1

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

j=0
while j<5:
   j+=1
   if j==3:
      continue
   print(j)

#looping through a list
fruits=["apple","banana","orange"]
for fruit in fruits:
   print(fruit)

#loopin through a string
for char in "banana":
   print(char)

#the break statement is used to exit a loop prematurely when a certain condition is met.
fruits=["melon","apples","grapes","pears"]
for fruit in fruits:
   if fruit=="grapes":
      break
   print(fruit)


#The continue statement is used to skip the current iteration of a loop and move on to the
cars=["BMW","Audi","Mercedes","Toyota","Honda"]
for car in cars:
   if car=="Mercedes":
      continue
   print(car)

"""The range() function returns a sequence of numbers, starting from 0 by default,
and increments by 1 (by default),and ends at a specified number."""
for x in range(5):
   print(x)

for x in range(0,37,3):
   print(x)
else:
   print("Finally finished!!!")

#Nested loops
adj=["red", "yellow", "green"] 
fruits=["apples","bananas","pears"]
for x in adj:
   for y in fruits:
      print(x,y)

#pass statement
for x in [0,1,2]:
   pass

# Iterating Over List, Tuple, String and Dictionary Using for Loops in Python

li = ["geeks", "for", "geeks"]
for x in li:
    print(x)
    
tup = ("geeks", "for", "geeks")
for x in tup:
    print(x)
    
s = "abc"
for x in s:
    print(x)
    
d = dict({'x':123, 'y':354})
for x in d:
    print("%s  %d" % (x, d[x]))
    
set1 = {10, 30, 20}
for x in set1:
    print(x),




#even numbers btween 1 and 100
for x in range(1,100):
   if x%2==0:
      print(x)
