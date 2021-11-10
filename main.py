import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Hoso",
  password="123456",
  database="bank uml"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM bank_account")
#mycursor.execute("SELECT * FROM bank_account")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)