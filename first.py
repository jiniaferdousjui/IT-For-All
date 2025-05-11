course = "Python Programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])
course_name = "python \"programming"
print(course_name)
# \'""
# how to separate lines
courses = "python \nprograme"
print(courses)
first = "Jinia"
last = "Jui"
full = f"{first} {last}"
print(full)
course = "Python program"
print(course.upper())
print(course.capitalize())
print(course.casefold())
print(course.strip())
print(course.find("pro"))
print(course.replace("p", "j"))
print("pro" in course)
print("sui" not in course)
x = 1 + 2j  # a + bi
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)
# x = 5
# x += 3
# print(x)
# x = input("x: ")
# print(type(x))
# y = x + 1
# x = input("x: ")
# y = int(x) + 1
# print(f"x: {x}, y: {y}")
fruit = "Apple"
print(fruit[1:-1])
temp = 3
if temp > 30:
    print("it's warm")
    print("drink water")
elif temp > 10:
    print("nice")
else:
    print("cold")
    # print("done")
age = 28
if age >= 25:
    message = "Eligible"
else:
    message = "Non Eligible"
print(message)
message = "Eligible" if age >= 30 else "Not Eligible"  # turnery operator
print(message)
# logical operator
# and: if both statement is true then the ans would be yes
high_cg = False
ielts_score = True
student = False
if high_cg and ielts_score:
    print("pass")
else:
    print("failed")
# or operator: if one will true result would be yes
if high_cg or ielts_score:
    print("ok")
else:
    print("not ok")
# multiple conditions
if (high_cg or ielts_score) and not student:
    print("fine")
else:
    print("not fine")
# short-circuit evaluation
# when it's connected with and operators if one statement is false it stops evaluating, in or operators if one statement is true it stops evaluating
# chaining comparison operators
age = 30
# if age <= 40 and age >= 20:
# print("ok") can be written as
if 20 <= age <= 40:
    print("ook")
# for loops
# to stop doing the same code we create a loop like:
for number in range(5):
    print("try again", number + 1, (number + 1) * ".")
for number in range(1, 10, 2):
    print("attempt", number, number * "/")
# rules of For...else that means opearation repeatation would stop if certain action happens
successful = False
for number in range(1, 4):
    print("nice try")
    if successful:
        print("successful")
        break
# if after trying this time and still failed and want to show a different message
else:
    print("Attempted 4 times and failed")
# nested loop
for x in range(1, 5):
    for y in range(1, 5):
        print(f"{x},{y}")
# iterable
for x in "Python":
    print(x)
for x in [1, 2, 3, 4]:  # [] means listing
    print(x)
students = ["jui", "jinia", "ferdous"]
for student in students:                 # if we did it manually it'd look like
    # students = ["jui","jinia","ferdous"]
    print("student's name", ":", student)
    # print("name",":",students[0])
    # print("name",":",students[1])
    # print("name",":",students[2])
# while loop : repeat something until a condition is true
number = 100
while number > 0:
    number //= 2
    print(number)
# need to open in terminal
command = ""
while command != "quit" and "QUIT":
    command = input(">")
    print("echo", command)
