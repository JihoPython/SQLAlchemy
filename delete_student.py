from dictionary.connector import session
from dictionary.student import Student

# DELETE
student = session.query(Student).filter(Student.name == 'Givenchy').first()
session.delete(student)
session.commit()
