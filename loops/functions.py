#fuctions use def keyword
#the syntanx is:
"""
def function_name(parameters):
    statement
    return value
"""
def fun():
    print("Welcome to functions")
fun()     #driver code for calling the function

def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))

#*args in Python (Non-Keyword Arguments)
#**kwargs in Python (Keyword Arguments)
def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

# Function call with both types of arguments
myFun('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks')