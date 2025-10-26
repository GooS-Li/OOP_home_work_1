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
        average = round(summary / len(value_list),2)
        return f"Средняя оценка студента {self.name} {self.surname} за все курсы равна: {average}"

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
                f"Средняя оценка за лекции: {self.average_grade_lecture()}\n")

    def average_grade_lecture(self):
        summary = 0
        grades = self.grades
        value_list = grades.values()
        for i in value_list:
            for j in i:
                summary += j
        average = round(summary / len(value_list),2)
        return f"Средняя оценка лектора {self.name} {self.surname} за все курсы равна: {average}"


class Reviewer(Mentor):
    def __init__(self, name,surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        self._rate_hw(student, course, grade)

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n")

def average_grade_lectures(lectures, course):
    if not isinstance(lectures, list):
        return "В функцию передается не список"
    all_average_grade = []
    for lecture in lectures:
        grade_lecture = lecture.grades
        all_average_grade.extend(grade_lecture.get(course))
    if not all_average_grade:
        return "По такому курсу ни у кого нет оценок"
    else:
        return (f"Средняя оценка лекторов в рамках курса {course} равна: "
                f"{round(sum(all_average_grade) / len(all_average_grade), 2)}")

def average_grade_students(students, course):
    if not isinstance(students, list):
        return "В функцию передается не список"
    all_average_grade = []
    for student in students:
        grade_student = student.grades
        all_average_grade.extend(grade_student.get(course))
    if not all_average_grade:
        return "По такому курсу ни у кого нет оценок"
    else:
        return (f"Средняя оценка студентов в рамках курса {course} равна: "
                f"{round(sum(all_average_grade) / len(all_average_grade), 2)}")

lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Василий', 'Петров')
reviewer1 = Reviewer('Пётр', 'Петров')
reviewer2 = Reviewer('Валерий', "Шагисултанов")
student_woman = Student('Алёхина', 'Ольга', 'Ж')
student_man = Student('Жаворонков', 'Василий', 'М')

student_man.courses_in_progress += ['Python', "Java", 'C++']
student_woman.courses_in_progress += ["Python", "Java",'C++']
lecturer1.courses_attached += ['Python', 'C++', 'Java']
lecturer2.courses_attached += ['Python', 'Java']
reviewer1.courses_attached += ['Python', 'Java']
reviewer2.courses_attached += ['Python', 'C++']

lectures = [lecturer1, lecturer2]
students = [student_man, student_woman]

student_man.rate_lecture(lecturer1, "Java", 9.9)
student_man.rate_lecture(lecturer2, "Python", 8.6)
student_woman.rate_lecture(lecturer2, "Java", 7.7)
student_woman.rate_lecture(lecturer1, "Python", 7.4)

reviewer1.rate_hw(student_man, "Python", 9.4)
reviewer1.rate_hw(student_man, "Java", 7.7)
reviewer1.rate_hw(student_woman, "Python", 8.9)
reviewer1.rate_hw(student_woman, "Java", 7.2)
reviewer2.rate_hw(student_man, "Python", 8.7)
reviewer2.rate_hw(student_man, "Python", 9.9)

print(lecturer1.average_grade_lecture())
print(lecturer2.average_grade_lecture())
print(student_man.average_grade_student())
print(student_woman.average_grade_student())
print(average_grade_lectures(lectures, "Python"))
print(average_grade_students(students, "Java"))




