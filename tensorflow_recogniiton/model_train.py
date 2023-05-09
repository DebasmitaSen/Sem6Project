import matplotlib.pyplot as plt
# import numpy as np
import PIL
# import tensorflow as tf
import pathlib
import cv2

path1=pathlib.Path("C:/Users\mouli/Documents/GitHub/Sem6Project")
path2="Data"
path2= pathlib.Path(path2)
data_dir=path1.joinpath(path2)
# print(data_dir)
image_count = len(list(data_dir.glob('*/*.jpg')))
# print(image_count)

r = list(data_dir.glob('22/*.jpg'))
st=cv2.imread(str(r[3]))
cv2.imshow('win',st)
cv2.waitKey(0)
# PIL.Image.open(str(r[3]))
