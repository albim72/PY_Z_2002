import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1', port='3306',database="dbtestowa")

cursorObject = db.cursor()
#cursorObject.execute("CREATE DATABASE dbtestowa")
# tblstudent = "CREATE TABLE student(imie VARCHAR(60),nazwisko VARCHAR(60), id int);"
# cursorObject.execute(tblstudent)

insdata = "INSERT INTO student(imie, nazwisko, id) VALUES(%s,%s,%s)"
val = [
    ("Jan","Kot",2424),
    ("Janusz","Kotek",5645),
    ("Janina","Kotik",24654624),
    ("Jolka","Kret",2476624)
]
cursorObject.executemany(insdata,val)
db.commit()

db.close()
