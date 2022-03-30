import mysql.connector

mydb = mysql.connector.connect(
       host= "192.168.1.3",
       user="barry",
       password="123"
#       database="Attendanceyt"

)
a = mydb.cursor()
a.execute("CREATE DATABASE Attendance")
#a.execute("CREATE TABLE UserAttendance (Date VARCHAR(30),USERNAME VARCHAR(255),DateTime VARCHAR(255), PRIMARY KEY (Date,USERNAME))")
# sql = "DROP DATABASE Attendanceyt"
# a.execute(sql)
mydb.commit()
mydb.close()