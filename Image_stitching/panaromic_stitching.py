import numpy as np
import cv2
import glob
import imutils
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = glob.glob(os.path.join(script_dir, "imgs/*.jpeg"))
print(image_path)
images = []

for image in  image_path:
    img =  cv2.imread(image)
    images.append(img)
    cv2.imshow("Image", img)
    cv2.waitKey(0)

imageSticher = cv2.Stitcher_create()

error, stitched_img = imageSticher.stitch(images)

if not error:
        cv2.imwrite("stitched_images.png", stitched_img)
        cv2.imshow("stitched images", stitched_img)
        cv2.waitKey(0)





