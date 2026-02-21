""""
2.1 Python as a Calculator

print(14 + 5)
print(14 / 3)  #Division
print(14 // 3)  #Floor Division
print(14 % 3)   #Modulus (remainder)
#print(2 ** 4)   #Power



2.1.1 Floating Point Expressions
x = 3.14
y = 2.5
print(x + y)
print(0.1 + 0.2)




2.2 Python Basics

2.2.1 Literal Constants

Literal = fixed value written directly in code.

10          # Integer
3.14        # Float
"Hello"     # String
True        # Boolean
None        # NoneType

print(type(True))  # Output: <class 'float'>


2.2.2 Numbers


a = 10
b = 3.5
c = 2 + 4j

print(type(c))

name = "venkatram"

# print(name[0])      # First letter
# print(name[5])     # Last letter
# print(len(name))    # Length
# print(name.upper())
# print(name.lower())
#print(name[0:4])

#string[start : end]

print("Hello World")
print("Age:", 25)
print("Fruits:", "Apple", "Banana", "Cherry")
print("A", "B", "C", sep="-")
print("Hello", end=" ")
print("World")


name = "Venkatram"
age = 35
location = "India"
print("Hello {}".format(name))
print(f"My name is {name} and I am {age} years old and i am from {location}")

print("Hello\nWorld")
print("Python\tProgramming")

if 2 == 2:
    print("Two is equal to two")
    
if 5 > 2:
    print("Five is greater")
    
    
age = 30
print(f"Next year you will be {age+1}.")

"""
