import cv2
import image_manupulation

arrays = image_manupulation.retrive()
classID=arrays[0]
names=arrays[1]
images=arrays[2]

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

for i in range(len(names) * 5):
    
    path=list3[i]
    print(path)
    imgx=cv2.imread(path)
    
    h, w, _ = imgx.shape

    # Find minimum dimension
    min_dim = min(h, w)

    # Calculate center of image
    center_h = h // 2
    center_w = w // 2

    # Calculate top-left corner of square
    x = center_w - min_dim // 2
    y = center_h - min_dim // 2

    # Crop image to square and resize to 180x180
    img_square = imgx[y:y+min_dim, x:x+min_dim]
    img_resized = cv2.resize(img_square, (180, 180))
#   
    cv2.imwrite(path, img_resized)




