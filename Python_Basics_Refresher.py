# Python Basics Cheat Sheet

# 1. Printing
print("Hello, World!")  # Outputs: Hello, World!

# 2. Variables
x = 10          # Integer
y = 3.14        # Float
name = "Alice"  # String
is_active = True  # Boolean

# 3. Indentation (Python uses spaces to define code blocks)
if x > 5:
    print("x is greater than 5")

# 4. Conditionals
if x > 5:
    print("x is large")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is small")

# 5. Loops
# For loop
for i in range(5):  # 0 to 4
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# 6. Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Outputs: Hello, Alice!

# 7. Lists
numbers = [1, 2, 3, 4, 5]
numbers.append(6)  # Add to list
print(numbers)     # Outputs: [1, 2, 3, 4, 5, 6]

# 8. Dictionaries
person = {"name": "Alice", "age": 30}
print(person["name"])  # Outputs: Alice

# 9. Classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name}"

p = Person("Alice", 30)
print(p.greet())  # Outputs: Hi, I'm Alice
