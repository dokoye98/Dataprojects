import numpy as np
import os.path
from  skimage.io  import imread
from skimage import data_dir

img = imread(os.path.join(data_dir,"Degreenew.jpg"))
print(img.size)
imt = img.T
print(imt)