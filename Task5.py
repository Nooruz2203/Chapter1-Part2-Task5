print ("Number of students in first class: ")
a = int(input())
print ("Number of students in second class: ")
b = int(input())
print ("Number of students in third class: ")
c = int(input())

x = a+b+c
y = (x // 2)+(x % 2)

print("Total number of students :", x, "students")
print("The number of desks we need", y, "desks.")
