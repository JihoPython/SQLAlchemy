from dictionary.connector import session
from dictionary.student import Student

# UPDATE
student = session.query(Student).filter(Student.name == 'uhuru').first()
student.name = 'Givenchy'

session.commit()
