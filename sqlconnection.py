import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql",
    database="employee"
)

# print("Connected successfully!")

conn=db.cursor()
conn.execute("select * from employee_details")
data=conn.fetchall()
for i in data:
    print(i[1],i[2])


conn.close()
db.close()

