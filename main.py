class Student():
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


cool_mentor = Mentor("Some", "Buddy")
cool_mentor.courses_attached += ["Python"]
print(cool_mentor.courses_attached)
cool_mentor.courses_attached += ["Golang"]
print(cool_mentor.courses_attached)

best_student = Student("Big", "Floppa", "Russian Cat")
best_student.finished_courses += ["C#"]
best_student.courses_in_progress += ["Python"]
best_student.grades["C#"] = [10, 8, 9, 10, 10]
best_student.grades["Python"] = [10, 10]
print(best_student.grades)