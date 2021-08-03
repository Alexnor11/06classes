class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def grade_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress \
                and course in lecturer.courses_mentored:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def same_grades(self):
        """ Вычисляет среднюю оценку за домашние задания """
        for grade in self.grades.values():
            result = round(sum(grade) / len(grade), 1)
            return result

    def __str__(self):
        res = f"\nИмя: {self.name}\nФамилия: {self.surname}\n" \
              f"Средняя оценка за домашние задания: {self.same_grades()}\n" \
              f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
              f"Завершенные курсы: {', '.join(self.finished_courses)}"
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor, Student):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_mentored = []
        self.grades = {}

    def __str__(self):
        res = f"\nИмя: {self.name}\nФамилия: {self.surname}\n" \
              f"Средняя оценка за лекции: {self.same_grades()}"
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"\nИмя: {self.name}\nФамилия: {self.surname}"
        return res


some_reviewer = Reviewer('Some1', 'Buddy')
some_reviewer.courses_attached += ['Python']

some_lecturer = Lecturer('Some2', 'Buddy')
some_lecturer.courses_mentored += ['Git', 'Python']

some_student = Student('Ruy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Git', 'Python']
some_student.finished_courses = ['Введение в программирование']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 10)

some_student.grade_lecture(some_lecturer, 'Git', 10)
some_student.grade_lecture(some_lecturer, 'Git', 10)
some_student.grade_lecture(some_lecturer, 'Git', 8)

print(some_reviewer)
print(some_lecturer)
print(some_student)
