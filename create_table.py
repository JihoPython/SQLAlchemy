from unicodedata import name
from dictionary.connector import engine, Base, session
# from dictionary.student import Student

def excute_ddl():
    Base.metadata.create_all(engine)
    session.commit()

if __name__ == '__main__':
    excute_ddl()
