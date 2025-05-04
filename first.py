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
