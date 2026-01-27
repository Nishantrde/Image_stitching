import numpy as np
import cv2
import glob
import imutils
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = glob.glob(os.path.join(script_dir, "imgs/*.jpeg"))
print(image_path)

