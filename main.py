
from datetime import date, datetime, timedelta
from university import Course, Mentor, Teacher, Student, University

python_course = Course("Python", datetime.now(), datetime.now() + timedelta(days=30))
js_course = Course("JavaScript", datetime.now(), datetime.now() + timedelta(days=60))

alex_student = Student("Alex", "Stp", date(1995, 7, 8))
nik_student = Student("Nik", "Fial", date(1998, 10, 22))

bred_teacher = Teacher("Bred", "Cmp", date(1974, 6, 25), 2000, python_course)

koli_mentor = Mentor("Koli", "Key", date(1987, 3, 13), 1200, [python_course, js_course])

harvard_university = University(
    "Harvard",
    [python_course, js_course],
    [bred_teacher, koli_mentor],
    [alex_student, nik_student],
)

print('COURSE')
print(python_course)
print(python_course.is_active())

print('TEACHER')
print(bred_teacher.answer_question(python_course, 'Про що цей курс?'))
print(bred_teacher.answer_question(js_course, 'Про що цей курс?'))
print(bred_teacher.change_course(js_course))
print(bred_teacher.answer_question(python_course, 'Про що цей курс?'))
print(bred_teacher.answer_question(js_course, 'Про що цей курс?'))
print(bred_teacher)
print(bred_teacher.get_yearly_salary())

print('MENTOR')
print(koli_mentor.answer_question(python_course, 'Про що цей курс?'))
print(koli_mentor.answer_question(python_course, 'Що це?'))
print(koli_mentor.answer_question(python_course, 'Як тебе звати?'))
print(koli_mentor.answer_question(python_course, 'Що це?'))
print(koli_mentor.answer_question(python_course, 'Що це?'))
print(koli_mentor.answer_question(python_course, 'Як тебе звати?'))
print(koli_mentor.answer_question(python_course, 'Як довго триватиме цей курс?'))
print(koli_mentor.answer_question(python_course, 'Як довго триватиме цей курс?'))
print(koli_mentor.answer_question(python_course, 'Як довго триватиме цей курс?'))
print('STUDENT')
alex_student.add_mark(8)
alex_student.add_mark(7)
alex_student.add_mark(10)
alex_student.add_mark(6)
alex_student.add_mark(11)

nik_student.add_mark(6)
nik_student.add_mark(9)
nik_student.add_mark(2)
nik_student.add_mark(5)
nik_student.add_mark(6)

print(alex_student.get_all_marks())
print(alex_student.get_avarage_mark())
print(alex_student.get_average_by_last_n_marks(4))
print(alex_student.get_average_from_date(datetime(2022, 7, 25, 0, 0, 0)))
print(alex_student)

print('UNIVERSITY')
print(harvard_university.get_average_mark())
print(harvard_university.get_active_courses())
print(harvard_university)
print(harvard_university.get_average_salary())
