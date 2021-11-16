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

###############
print("max_withrow_amount	")
mycursor.execute("SELECT * FROM current_acount WHERE max_withrow_amount	> 16000")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

  ####################

print("find name")
mycursor.execute("SELECT * FROM buisnessclient WHERE director_name	LIKE '%r%'")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

print("copy from xammpp")
mycursor.execute("SELECT * FROM `bank_account` WHERE `contractbalance` != '50000'")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

###########################
print("order by")
mycursor.execute("SELECT * FROM `client` ORDER BY name")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

##############
mycursor = mydb.cursor()
sql = "INSERT INTO client(name, adress ,phone_number , email ) VALUES (%s , %s , %s , %s )"
val = ("Vahe", "Yerevan vardanants 5" , "055987654" , "Vahe@yahoo.com")
mycursor.execute(sql , val)
mydb.commit()
print(mycursor.rowcount, "record inserted")