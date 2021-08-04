class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def grade_lecture(self, lecturer, course, grade):
        """Оценка лекторам от учеников"""
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
              f"Завершенные курсы: {', '.join(self.finished_courses)}\n"
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

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Нет оценок')
            return
        return self.same_grades() >= other.same_grades()


class Reviewer(Mentor):
    """Выставление оценок студентам"""

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


# Полевые испытания:
print("\nЗадание №4. Полевые испытания:")


# Та же задача по оценкам, только реализована с одной функцией
def average_rating(course, *args):
    """Срелняя оцека по студентам"""
    avr_grade_student = 0
    num_students = 0
    mark = 0

    for i in args:
        if i.grades.get(course):
            sum_grade = sum(i.grades[course]) / len(i.grades[course])
            num_students += 1
            mark += sum_grade
        if num_students != 0:
            avr_grade_student = mark / num_students
        print(f"Средняя оценка по {course}: {avr_grade_student}")


# def grade_lecturer(course, *lecturers):
#     """Средняя оцека по лекторам"""
#     avr_grade_lecturers = 0
#     num_lecturers = 0
#     mark = 0
#
#     for i in lecturers:
#         if i.grades.get(course):
#             sum_grade = round(sum(i.grades[course]) / len(i.grades[course]), 1)
#             num_lecturers += 1
#             mark += sum_grade
#         if num_lecturers != 0:
#             avr_grade_lecturers = mark / num_lecturers
#         print(f"Средняя оценка Лекторов по {course}: {avr_grade_lecturers}")


# Студенты
flow_one_student = Student('Oleg', 'Shishkin', 'man')
flow_one_student.finished_courses = ['Python']
flow_two_student = Student('Natasha', 'Queen', 'woman')
flow_two_student.finished_courses = ['Git']

flow_one_student.courses_in_progress += ['Git', 'Python']
flow_two_student.courses_in_progress += ['Git', 'Python']

# Лекторы
python_lecturer = Lecturer('Maxim', 'Galkin')
git_lecturer = Lecturer('Alisa', 'Selezneva')

python_lecturer.courses_mentored += ['Python']
git_lecturer.courses_mentored += ['Git']

# Оцеки лекторам
flow_one_student.grade_lecture(python_lecturer, 'Python', 10)
flow_one_student.grade_lecture(python_lecturer, 'Python', 9)
flow_two_student.grade_lecture(git_lecturer, 'Git', 9)
flow_two_student.grade_lecture(git_lecturer, 'Git', 8)

# Проверяющии
python_reviewer = Reviewer('Sasha', 'Ivanov')
git_reviewer = Reviewer('Petya', 'Vasechkin')

python_reviewer.courses_attached += ['Python']
git_reviewer.courses_attached += ['Git']

# Оцеки студентам
python_reviewer.rate_hw(flow_one_student, 'Python', 9)
git_reviewer.rate_hw(flow_two_student, 'Git', 9)
git_reviewer.rate_hw(flow_two_student, 'Git', 8)

print(python_reviewer)
print(git_reviewer)

print(python_lecturer)
print(git_lecturer)

print(flow_one_student)
print(flow_two_student)

print('Студенты:')
average_rating('Python', flow_one_student)
average_rating('Git', flow_two_student)
print('Лкторы:')
average_rating('Python', python_lecturer)
average_rating('Git', git_lecturer)
