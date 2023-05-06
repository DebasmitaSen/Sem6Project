import mysql.connector
import os
# import shutil
import db_conn
import db_execute_query

def insert_to_db():

   # establish a MySQL connection
   db = db_conn.create_db_connection("localhost", "root", "", "person")
   # mysql.connector.connect(
   #    host="localhost",
   #    user="root",
   #    passwd="",
   #    database="person"
   # )
   query_1 = "CREATE TABLE IF NOT EXISTS images (id INT(15), Name VARCHAR(255),Image VARCHAR(250),PRIMARY KEY(id) )"
   cursor = db.cursor()
   cursor.execute(query_1)

   # folder_path = "D:/Face recognization project/Sem6Project/Input/"
   # parent_dir="D:/Face recognization project/Sem6Project/Data/"
   folder_path = "C:/Users/mouli/Documents/GitHub/Sem6Project/Input"
   parent_dir="C:/Users/mouli/Documents/GitHub/Sem6Project/Data"

   image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]


   for filename in image_files:
      if not os.path.isdir("Data"):
         os.mkdir("Data")

      
      with open(os.path.join(folder_path, filename), "rb") as f:
         
         
         words = filename.split('-')
         img_id=words[0].split('_')
         name=img_id[0]
         Id=img_id[1]
         photonum=words[1].split(".")
         
         Iddir_path=os.path.join(parent_dir,img_id[1])
         if not os.path.isdir(Iddir_path):
            os.makedirs(Iddir_path)
         img_path = 'Data/'
         img_path = img_path + Id
         try:
            query = "INSERT INTO images (id,Name,Image) VALUES (%s,%s,%s)"
            values = (Id,name,img_path)
            cursor.execute(query, values)
            db.commit()
            query_2 = "insert into total_attendence(id, name, total_att) values (%s, %s, 0)"
            value = (Id, name)
            cursor.execute(query_2, value)
            db.commit()
         except:
            pass
         f.close()
         
         os.rename(os.path.join(folder_path, filename),os.path.join(Iddir_path,"img"+photonum[0]+".jpg"))
         # print("Image {} has been inserted into the database with id {}".format(filename, cursor.lastrowid))
   db.close()     


def retrive():
   db = db_conn.create_db_connection("localhost", "root", "", "person")
   query2="SELECT id,Name,Image FROM images"
   # cursor.execute(query2)
   classID=[]
   names=[]
   images=[]
   # result=cursor.fetchall()
   result = db_execute_query.read_query_(db, query2)
   db.close()
   lengh=len(result)
   for x in range (lengh) :
      c,n,i=result[x]
      classID.append(c)
      names.append(n)
      images.append(i)
   return  classID,names,images

# arrays=retrive()

# classID=arrays[0]
# names=arrays[1]
# images=arrays[2]
# print(classID)

def crbk():
  folder_path = "D:/Face recognization project/Sem6Project/Input/"
  image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
  for filename in image_files:
    if os.path.isdir(os.path.join(folder_path, filename)):
     os.remove(os.path.join(folder_path, filename))

# close the database connection
# db.close()
#retrive()
# crbk()
