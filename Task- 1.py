# Question 1: Student Marks Manager

marks = []

for i in range(3):
    mark = int(input("Enter mark: "))
    marks.append(mark)

print("\nOriginal marks:", marks)

marks.insert(0, 90)
print("After inserting 90:", marks)

marks.extend([75, 85])
print("After adding 75 and 85:", marks)

if 75 in marks:
    marks.remove(75)
    print("75 was removed.")

removed_mark = marks.pop()
print("Removed final mark:", removed_mark)

print("Final marks:", marks)
print("Number of marks:", len(marks))


# Question 2: Number List Analyser

numbers = [20, 10, 30, 20, 40, 20]

numbers.sort()
print("\nAscending order:", numbers)

numbers.reverse()
print("Descending order:", numbers)

search_number = int(input("\nEnter a number to search: "))

if search_number in numbers:
    print("Number found.")
    print("Count:", numbers.count(search_number))
    print("First index:", numbers.index(search_number))
else:
    print("Number not found.")

print("\nSmallest value:", min(numbers))
print("Largest value:", max(numbers))
print("Total:", sum(numbers))


# Question 3: Even and Odd Number Separator

numbers = [10, 15, 20, 25, 30, 35]

even = []
odd = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print("\nEven numbers:", even)
print("Odd numbers:", odd)

print("First three values:", numbers[:3])
print("Last three values:", numbers[-3:])

backup = numbers.copy()

numbers.clear()

print("Original list after clear():", numbers)
print("Backup list:", backup)


# Question 4: Unique Name Manager

names = ["Asha", "Rahul", "Asha", "John", "Rahul"]

unique_names = set(names)

print("\nUnique names:", unique_names)

unique_names.add("Meera")

unique_names.update(["Arun", "Priya"])

if "John" in unique_names:
    unique_names.remove("John")
    print("John was removed.")

unique_names.discard("David")

print("\nFinal unique names:")

for name in unique_names:
    print(name)


# Question 5: Course Student Comparison

python_students = {"Asha", "Rahul", "John", "Meera"}
da_students = {"Rahul", "Meera", "Arun"}

all_students = python_students.union(da_students)

print("\nAll students from both courses:")
for student in all_students:
    print(student)

both_courses = python_students.intersection(da_students)

print("\nStudents learning both courses:")
for student in both_courses:
    print(student)

only_python = python_students.difference(da_students)

print("\nStudents learning only Python:")
for student in only_python:
    print(student)

only_one_course = python_students.symmetric_difference(da_students)

print("\nStudents learning only one course:")
for student in only_one_course:
    print(student)

if da_students.issubset(python_students):
    print("\nDA students are a subset of Python students: True")
else:
    print("\nDA students are a subset of Python students: False")

if python_students.issuperset(da_students):
    print("Python students are a superset of DA students: True")
else:
    print("Python students are a superset of DA students: False")

if python_students.isdisjoint(da_students):
    print("The two sets are disjoint: True")
else:
    print("The two sets are disjoint: False")
