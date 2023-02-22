import mysql.connector
import sqlalchemy
from sqlalchemy.orm import DeclarativeBase


engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:abc123@localhost:3306/dbtestowa', echo=True)
class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_account"
    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=50))
    fullname = sqlalchemy.Column(sqlalchemy.String(length=50))
    nickname = sqlalchemy.Column(sqlalchemy.String(length=50))

    def __repr__(self):
        return f"<User(name={self.name}, fullname={self.fullname}, nickname={self.nickname})>"

Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

u1 = User(name="Marcin", fullname="Marcin Albiniak", nickname = "albim")
session.add(u1)

u2 = User(name="Olga", fullname="Olga Kot", nickname = "kota")
session.add(u2)

u3 = User(name="Tomasz", fullname="Tomasz Nowak", nickname = "tom")
session.add(u3)

session.commit()

print("Wszyscy użytkownicy: ")
for s in session.query(User).all():
    print(s.fullname,s.nickname)

print("Użytkownik tom: ")
for s in session.query(User).filter(User.nickname == "tom"):
    print(s.fullname,s.nickname)



