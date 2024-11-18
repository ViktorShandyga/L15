class Human:
    height = 170
    salary = 0
class Student(Human):
    pass
class Worker(Human):
    salary = 500
nick = Student()
ann = Worker()
print(nick.height, "cm")
print(ann.height, "cm")
print(ann.salary, "$")
print(nick.salary, "$")