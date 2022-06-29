from create_table import excute_ddl

from dictionary.connector import session
from dictionary.student import Student


try:
    session.query(Student).first()
    raise Exception()
except:
    excute_ddl()


student_1 = Student(name='Jiho', age=29, grade='Junior')
student_2 = Student(name='uhuru', age=23, grade='A')
student_3 = Student(name='jihogrammer', age=24, grade='B')

session.add(student_1)
session.add_all([student_2, student_3])

session.commit()
