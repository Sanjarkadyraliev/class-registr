class Human():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Human):
    def __init__(self, name, age, subject, exp):
        super().__init__(name, age)
        self.subject = subject
        self.exp = exp
class Student(Human):
    def __init__(self, name, age, grade, adress):
        super().__init__(name, age)
        self.grade = grade
        self.adress = adress
def new_person():
    name = input("enter your name: ")
    age = int(input("enter your age: "))
    return [name, age]
def teacher_reg():
    subject = input("enter your subject: ")
    exp = int(input("enter exp: "))
    return [subject, exp]
def student_reg():
    grade = int(input("enter your grade: "))
    adress = input("enter your adress: ")
    return [grade, adress]

def check_position():
    position =input("Are you teacher or student?: ").capitalize()
    while True:
        if position == "Teacher" or position == "Student":
            break
        position = input("enter only teacher or student").capitalize()
    personal_info = new_person()
    if position == "Teacher":
        personal_info += teacher_reg()
    elif personal_info == "Student":
        personal_info += student_reg()
        personal_info = new_person()
    return personal_info
def main():
    personal_info = check_position()
    if personal_info[0] =="Teacher":
        teacher = Teacher(personal_info[1], personal_info[2], personal_info[3], personal_info[4])
        return teacher
    elif personal_info[0] == "Student":
        student = Student(personal_info[1], personal_info[2], personal_info[3], personal_info[4])
        return student
teacher = main()
student = main()
print(teacher.name, teacher.age)
print(student.name, student.age)
