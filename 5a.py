students=dict()
n=int(input("enter the number of students:"))
for i in range(n):
    sname=input("enter the name of student:")
    rollno=input("enter the roll number of the student:")
    branch=input("enter the branch of student:")
    marks=input("enter the marks of student:")
    age=input("enter the age of student:")

    students[sname]=rollno,branch,marks,age
print("the created dictionaries of students:",students)
print("after sorting",sorted(students.items()))
print("after sorting",sorted(students.values()))
