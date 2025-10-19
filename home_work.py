class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached
                and course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade_student(self):
        summary = 0
        grades = self.grades
        value_list = grades.values()
        for i in value_list:
            for j in i:
                summary += j
        average = summary / len(value_list)
        return average

    def __str__(self):
        course_in_progress = ", ".join(self.courses_in_progress)
        finished_courses = ", ".join(self.finished_courses)
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.average_grade_student()}\n"
                f"Курсы в процессе изучения: {course_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def _rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name,surname):
        self.grades = {}
        super().__init__(name, surname)

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.average_grade()}\n")

    def average_grade(self):
        summary = 0
        grades = self.grades
        value_list = grades.values()
        for i in value_list:
            for j in i:
                summary += j
        average = summary / len(value_list)
        return average



class Reviewer(Mentor):
    def __init__(self, name,surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        self._rate_hw(student, course, grade)

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n")



lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java', 'C++']
lecturer.courses_attached += ['Python', 'C++', 'Java']
reviewer.courses_attached += ['Python', 'C++']

reviewer.rate_hw(student, "Python", 9.8)
reviewer.rate_hw(student, "C++", 7.3)


student.rate_lecture(lecturer, 'Python', 9.8)  # None
student.rate_lecture(lecturer, 'Java', 8.8) # Ошибка
student.rate_lecture(lecturer, 'С++', 8)  # Ошибка
student.rate_lecture(reviewer, 'Python', 6)

print(reviewer)
print(lecturer)
print(student)




