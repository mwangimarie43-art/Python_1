# If Conditional Statement
# If statement is the simplest form of a conditional statement. 
# It executes a block of code if the given condition is true.
age = 20
if age >= 18:
    print("Eligible to vote.")


"""If Else allows us to specify a block of code that will execute 
if the condition(s) associated with an if or elif statement evaluates to False. 
Else block provides a way to handle all other cases that don't meet the specified conditions. """
age = 10
if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")


""""elif statement in Python stands for "else if."
 It allows us to check multiple conditions, providing a way to execute different blocks of code based on which condition is true.
 Using elif statements makes our code more readable and efficient by eliminating the need for multiple nested if statements."""
age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")


"""Nested if..else Conditional Statement
Nested if..else means an if-else statement inside another if statement. 
We can use nested if statements to check conditions within conditions."""
age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
      print("Not eligible for a senior discount.")

# Exercise: Conditional Statements
#Question 1
# Write a program that checks if a number entered by the user is positive, negative, or zero.
num=int(input("Enter a number:"))

if num==0:
    print("The number is zero") 
elif num>0:
    print("The number is positive")
else:
    print("The number is neative")

#Question 2
"""2.Ask the user for their age and print:
“You are a minor” if age < 18
“You are an adult” if age ≥ 18"""

age=int(input("Enter your age:"))

if age<18:
    print("You are a minor") 
else:
    print("You are an adult")


#Question 3
"""Write a program that asks for a score (0–100) and prints the grade:

90–100 → “A”

80–89 → “B”

70–79 → “C”

60–69 → “D”

<60 → “F”  """

score=int(input("Enter your score:"))
if score>=90 and score<=100:
    print("Grade: A")
elif score>=80 and score<=89:
    print("Grade: B")
elif score>=70 and score<=79:
    print("Grade: C")
elif score>=60 and score<=69:
    print("Grade: D")
else:
    print("Grade: F")

 

#Question 4
"""Ask the user to input a day of the week and print whether it’s a weekday or weekend."""
day=str(input("Enter a day of the week:"))
if day.lower() in ["saturday", "sunday"]:      #in is to check if a value exists within a sequence or collection
    print("It's a weekend.")    
else:
    print("It's a weekday.")

#Question 5
"""Ask the user for a number. If the number is positive,
 check if it’s even or odd."""
mynum=int(input("Enter a number:"))
if mynum>0:
    if mynum%2==0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("the number is negative or zero.")

    
#Question 6
"""Write a program to determine if a year is a leap year.

Leap year if divisible by 4 but not 100, unless divisible by 400."""

year=int(input("Enter a year:"))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")



#Question 7
#Write a program that asks for three numbers and prints the largest.
num1=float(input("Enter num1:"))
num2=float(input("Enteru num2:"))
num3=float(input("Enter num3:"))

if num1>=num2 and num1>=num3:
    print(f"The largest number is: {num1}")
elif num2>=num1 and num2>=num3:
    print(f"The largest number is: {num2}")
else:
    print(f"The largest number is: {num3}")

#Question 8
"""Ask the user for a number and print:

“Fizz” if divisible by 3

“Buzz” if divisible by 5

“FizzBuzz” if divisible by both 3 and 5

The number itself if divisible by neither"""
num=int(input("Enter Num:"))
if num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")
elif num%3==0 and num%5==0:
    print("FizzBuzz")
else:
    print(num)