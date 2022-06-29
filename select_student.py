from sqlalchemy import or_
from dictionary.connector import session
from dictionary.student import Student

print('------------------------------------------')
print('[select all]')

students = session.query(Student)
for student in students:
    print(student.name, student.age, student.grade)

print('------------------------------------------')
print('[order by]')

students = session.query(Student).order_by(Student.name)
for student in students:
    print(student.name, student.age, student.grade)

print('------------------------------------------')
print('[filter]')

student = session.query(Student).filter(Student.name == 'Jiho').first()
print(student.name, student.age, student.grade)

students = session.query(Student).filter(or_(Student.name == 'Jiho', Student.name == 'uhuru'))
for student in students:
    print(student.name, student.age, student.grade)

print('------------------------------------------')
print('[aggregate]')

students_count = session.query(Student).filter(or_(Student.name == 'Jiho', Student.name == 'uhuru')).count()

print('students_count', students_count)
