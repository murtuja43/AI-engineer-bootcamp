# variables and basic syntax
x = 10
y = 5
name = "Kayes"

print(x + y)
print(name)

# type checking
print(type(x))
print(type(name))

# basic math
a = 20
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)


# -------------------------------------------


# functions
def greet(person):
    return f"Hello, {person}"

print(greet("Kayes"))

def add(a, b):
    return a + b

print(add(10, 20))


# -------------------------------------------



# conditionals
num = 15

if num > 10:
    print("Greater than 10")
elif num == 10:
    print("Equal to 10")
else:
    print("Less than 10")


# -------------------------------------------


# lists
numbers = [1, 2, 3, 4, 5]

print(numbers[0])
print(numbers[-1])

numbers.append(6)
numbers.remove(3)

print(numbers)

# list iteration
for n in numbers:
    print(n)

# list comprehension
squares = [n**2 for n in numbers]
print(squares)


# -------------------------------------------


# loops
for i in range(5):
    print(i)

count = 0
while count < 5:
    print(count)
    count += 1


# -------------------------------------------


# strings
text = "hello world"

print(text.upper())
print(text.lower())
print(text.title())

print(text[0])
print(text[-1])

print(text.split())

# string formatting
age = 21
msg = f"My name is {name} and I am {age} years old"
print(msg)


# -------------------------------------------


# dictionaries
student = {
    "name": "Khaeys",
    "age": 21,
    "country": "Bangladesh"
}

print(student["name"])
print(student.get("age"))

student["age"] = 22
student["university"] = "Kazakhstan"

print(student)

for key, value in student.items():
    print(key, value)


# -------------------------------------------


# string exercise
word = "kaggle"

reversed_word = word[::-1]
print(reversed_word)

vowels = "aeiou"
count = 0

for letter in word:
    if letter in vowels:
        count += 1

print(count)

# list exercise
nums = [4, 2, 9, 1, 7]

largest = nums[0]

for n in nums:
    if n > largest:
        largest = n

print(largest)

even_numbers = []

for n in nums:
    if n % 2 == 0:
        even_numbers.append(n)

print(even_numbers)




# Done (Took around 2-3 hours to complete)