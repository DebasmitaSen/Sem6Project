import tensorflow as tf
import numpy as np
import cv2
import os
import connection
import attendence


arrays = connection.retrive()
classID=arrays[0]
names=arrays[1]
images=arrays[2]
name2=[]
classid=[]
for i in range(len(names)):
    for j in range(5):
        name2.append(names[i])
        classid.append(classID[i])
        
list1 = images
var="/img"
list2=[]
list3=[]
for i in  range (1,6):
    cn="%s"%i
    var2=var+cn+".jpg"
    list2.append(var2)
for i in range (len(list1)):
    for j in range (len(list2)):
        var3=list1[i]+list2[j]
        list3.append(var3)
imagelist=[]

for i in range(15):
    path=list3[i]
    imgx=cv2.imread(path)
    imagelist.append(imgx)


train_images=np.asarray(imagelist).astype(np.float32)
train_labels=np.asarray(classid).astype(np.float32)

test_images=np.asarray(imagelist).astype(np.float32)
test_labels=np.asarray(classid).astype(np.float32)
 

# Define the CNN architecture
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(224, 224, 3)),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    tf.keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    tf.keras.layers.Conv2D(128, kernel_size=(3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    tf.keras.layers.Conv2D(256, kernel_size=(3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(128)
])
#Compile mopdel
model.compile(optimizer='adam', loss='mse')

#Train model
model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))

model.save('face_recognition_model.h5')