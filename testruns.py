import matplotlib.pyplot as plt
# import numpy as np
import PIL
# import tensorflow as tf
import pathlib

path1=pathlib.Path("C:/Users\mouli/Documents/GitHub/Sem6Project")
path2="Data"
path2= pathlib.Path(path2)
data_dir=path1.joinpath(path2)
# print(data_dir)
image_count = len(list(data_dir.glob('*/*.jpg')))
# print(image_count)

r = list(data_dir.glob('22/*.jpg'))
print(str(r[3]))
PIL.Image.open(str(r[3]))
