import mysql.connector
import os
import shutil



# establish a MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="person"
)


cursor = db.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS images (id INT(15), Name VARCHAR(255),Image VARCHAR(250),PRIMARY KEY(id) )")


folder_path = "Input/"
parent_dir="Data/"

image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]


for filename in image_files:
    if not os.path.isdir("Data"):
      os.mkdir("Data")

    
    with open(os.path.join(folder_path, filename), "rb") as f:
        
        
        words = filename.split('-')
        img_id=words[0].split('_')
        name=img_id[0];
        Id=int(img_id[1])
        print(words[1][0])
        
        Iddir_path=os.path.join(parent_dir,img_id[1])
        if not os.path.isdir(Iddir_path):
           os.makedirs(Iddir_path)
        
        try:
          query = "INSERT INTO images (id,Name,Image) VALUES (%s,%s,%s)"
          values = (Id,name,Iddir_path)
          cursor.execute(query, values)
          db.commit()
        except:
           pass
        f.close()
        shutil.copy(os.path.join(folder_path, filename),Iddir_path)
        os.rename(os.path.join(Iddir_path, filename),os.path.join(Iddir_path,"img"+words[1][0]+".jpg"))
        print("Image {} has been inserted into the database with id {}".format(filename, cursor.lastrowid))
        db.close()


def retrive():
  
   query2="SELECT id,Image FROM images"
   cursor.execute(query2)
   classID=cursor.fetchall('Image')
   images=cursor.fetchall('id')
   print(classID)
   print(images) 
   
def crbk():
   shutil.move("Input/","Backup/")
   os.mkdir('Input')
#retrive()
crbk()
# close the database connection
