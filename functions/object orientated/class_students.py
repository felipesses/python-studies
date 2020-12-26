class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 - 100

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)  # Append in students array
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)


student = Student("Felipe", 20, 80)
student2 = Student("Tony", 22, 90)
student3 = Student("Lara", 19, 75)

course = Course("Math", 2)

course.add_student(student)
course.add_student(student2)
course.add_student(student3)

print(course.students)

print(course.get_average_grade())
