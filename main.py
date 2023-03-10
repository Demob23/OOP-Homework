def get_average_grades(grades):
    average_grade = 0
    num_of_sums = 0
    for key in grades:
        for grade in grades[key]:
            average_grade += grade
            num_of_sums += 1
    return average_grade / num_of_sums


def calculate_students_average_grades(students: list, course):
    average_grade = 0
    num_of_sums = 0
    for student in students:
        if course in student.courses_in_progress:
            for grade in student.grades[course]:
                average_grade += grade
                num_of_sums += 1
    average_grades = average_grade/num_of_sums
    return average_grades


def calculate_lectors_average_grades(lectors: list, course):
    average_grade = 0
    num_of_sums = 0
    for lector in lectors:
        if course in lector.courses_attached:
            for grade in lector.grades[course]:
                average_grade += grade
                num_of_sums += 1
    average_grades = average_grade/num_of_sums
    return average_grades


class Student():
    def __eq__(self, other):
        if isinstance(other, Student):
            return get_average_grades(self.grades) == get_average_grades(other.grades)
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Student):
            return get_average_grades(self.grades) != get_average_grades(other.grades)
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Student):
            return get_average_grades(self.grades) < get_average_grades(other.grades)
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, Student):
            return get_average_grades(self.grades) <= get_average_grades(other.grades)
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Student):
            return get_average_grades(self.grades) > get_average_grades(other.grades)
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Student):
            return get_average_grades(self.grades) >= get_average_grades(other.grades)
        else:
            return NotImplemented
    def __str__(self):
        return f"??????: {self.name}\n" \
               f"??????????????: {self.surname}\n" \
               f"?????????????? ???????????? ???? ???????????????? ??????????????: {get_average_grades(self.grades)}\n" \
               f"?????????? ?? ???????????????? ????????????????: {''.join(self.courses_in_progress)}\n" \
               f"?????????????????????? ??????????: {''.join(self.finished_courses)}"

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "????????????"


class Mentor():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return get_average_grades(self.grades) == get_average_grades(other.grades)
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return get_average_grades(self.grades) != get_average_grades(other.grades)
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return get_average_grades(self.grades) < get_average_grades(other.grades)
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return get_average_grades(self.grades) <= get_average_grades(other.grades)
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return get_average_grades(self.grades) > get_average_grades(other.grades)
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return get_average_grades(self.grades) >= get_average_grades(other.grades)
        else:
            return NotImplemented
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def __str__(self):
        return f"??????: {self.name}\n" \
               f"??????????????: {self.surname}\n" \
               f"?????????????? ???????????? ???? ????????????: {get_average_grades(self.grades)}"

class Reviewer(Mentor):
    def __str__(self):
        return f"??????: {self.name}\n" \
               f"??????????????: {self.surname}"
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "????????????"



student_1 = Student("??????????????", "??????????????????", "M")
student_2 = Student("????????????????????", "??????????????", "F")
lecturer_1 = Lecturer("????????????", "??????????????????")
lecturer_2 = Lecturer("??????????", "??????????????")
reviewer_1 = Reviewer("????????", "??????????????")
reviewer_2 = Reviewer("????????????", "????????????????????")

student_1.finished_courses += ["C#"]
student_1.courses_in_progress += ["Python", "Go"]

student_2.finished_courses += ["Java"]
student_2.courses_in_progress += ["Python"]

lecturer_1.courses_attached += ["Python"]
lecturer_2.courses_attached += ["Go", "Python"]

reviewer_1.rate_hw(student_1, "Python", 10)
reviewer_1.rate_hw(student_1, "Python", 9)
reviewer_1.rate_hw(student_1, "Go", 9)
reviewer_1.rate_hw(student_1, "Python", 10)
reviewer_1.rate_hw(student_1, "Python", 10)
reviewer_1.rate_hw(student_1, "Python", 10)
reviewer_1.rate_hw(student_1, "Go", 10)

reviewer_1.rate_hw(student_2, "Python", 8)
reviewer_1.rate_hw(student_2, "Python", 9)
reviewer_1.rate_hw(student_2, "Python", 10)

reviewer_2.rate_hw(student_1, "Python", 9)
reviewer_2.rate_hw(student_1, "Python", 9)
reviewer_2.rate_hw(student_1, "Python", 9)
reviewer_2.rate_hw(student_1, "Python", 10)
reviewer_2.rate_hw(student_1, "Python", 8)
reviewer_2.rate_hw(student_1, "Python", 8)
reviewer_2.rate_hw(student_1, "Python", 10)

reviewer_2.rate_hw(student_2, "Python", 8)
reviewer_2.rate_hw(student_2, "Python", 9)
reviewer_2.rate_hw(student_2, "Python", 10)

student_1.rate_lecture(lecturer_2, "Go", 8)
student_1.rate_lecture(lecturer_1, "Python", 10)
student_1.rate_lecture(lecturer_2, "Go", 10)

student_2.rate_lecture(lecturer_1, "Python", 8)
student_2.rate_lecture(lecturer_1, "Python", 10)
student_2.rate_lecture(lecturer_1, "Python", 10)

print(reviewer_1)
print(reviewer_2)
print(lecturer_1)
print(lecturer_2)
print(student_1)
print(student_2)
print(student_1 > student_2)
print(student_1 < student_2)
print(student_2 > student_1)
print(lecturer_1 == lecturer_2)
print(lecturer_1 != lecturer_2)
print(calculate_students_average_grades([student_1, student_2], "Go"))
print(calculate_lectors_average_grades([lecturer_1, lecturer_2], "Go"))