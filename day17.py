#1 create connection for db and print version
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Big_Data_Engineer")
cursor=mydb.cursor()
cursor.execute("SELECT VERSION()")
data=cursor.fetchone()
print("database version : ",data)
mydb.close()
#2 create multiple table and insert data inside table
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Big_Data_Engineer",database="TESTDB")

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))") #create table
mycursor.execute("SHOW TABLES")     #show tables in db

for x in mycursor:     
  print(x)

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
#3 create employee table and read all employee in the table using for loop
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Big_Data_Engineer",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE EMP(FNAME VARCHAR(30),LNAME VARCHAR(30),AGE INTEGER,INCOME INTEGER)")
sql= "INSERT INTO EMP(FNAME ,LNAME ,AGE,INCOME ) VALUES (%s, %s ,%s,%s)"
val= [("John", "smith",30,6000),("sandy", "richard",20,8000),("John", "william",40,6000),("susan", "smith",22,5000)]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
mycursor.execute("SELECT FNAME,LNAME FROM EMP") #selecting names in emp table

myresult = mycursor.fetchall()    

for x in myresult:              # reading names from emp table using for loop
  print(x)




