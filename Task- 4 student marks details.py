#task
#Creat a function withe usage of *args & **Kwargs with real time secenrio

def student_marks(*args, **kwargs):
    """Here takes student name marks and college and bank detals"""
    for student in args:
        print("Name:", student[0])
        print("Python:", student[1])
        print("SQL:", student[2])
        print("Java:", student[3])
        print()

    print("College:", kwargs["college"])
    print("Branch:", kwargs["branch"])


student_marks(
    ("Rohith", 85, 90, 80),
    ("Shanthi", 90, 88, 85),
    college="Andhra University",
    branch="Computer Science"
)
