import mysql.connector
import os

list=os.listdir('Input/')


Db = mysql.connector.connect(
  host ="localhost",
  user="root",
  password ="",
  database="person"
)

Mycursor = Db.cursor()
Mycursor.execute("CREATE TABLE IF NOT EXISTS Images (id INTEGER(45) NOT NULL AUTO_INCREMENT PRIMARY KEY, Photo LONGBLOB NOT NULL)")

def InsertBlob(Path):
    with open(Path, "rb") as File:
        BinaryData = File.read()
    SQLStatement = "INSERT INTO Images (Photo) VALUES (%s)"  
    Mycursor.execute(SQLStatement, (BinaryData, ))
    Db.commit()

def RetrieveBlob(ID):
    SQLStatement2 = "SELECT * FROM Images WHERE id='{0}'"
    Mycursor.execute(SQLStatement2.format(str(ID)))
    Bvalue = Mycursor.fetchone()[1] 
    store="Output/img{0}.jpg".format(str(ID))
    print(Bvalue)
    with open(store,"wb") as file:
        file.write(Bvalue)
        file.close()
    

for i in range (len(list)):    
    Way="Input/{0}".format(list[i])

    InsertBlob(Way)

for y in range (len(list)):
    
    RetrieveBlob(y+1)