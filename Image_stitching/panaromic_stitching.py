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
        cv2.imwrite("./stitched_images.png", stitched_img)
        cv2.imshow("stitched images", stitched_img)
        cv2.waitKey(0)
        stitched_img = cv2.copyMakeBorder(stitched_img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, (0,0,0))

        gray = cv2.cvtColor(stitched_img, cv2.COLOR_BGR2GRAY)
        thresh_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]

        cv2.imshow("Threshold Image", thresh_img)

        contours = cv2.findContours(thresh_img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)

        if len(contours) == 0:
            print("No contours found in threshold image; saving original stitch.")
            cv2.imwrite("stitchedOP.png", stitched_img)
            cv2.imshow("stitched output", stitched_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            raise SystemExit

        # Start from the largest contour of the mask
        areaOI = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(areaOI)

        # Build a mask for erosion-based tight crop
        mask = np.zeros(thresh_img.shape, dtype="uint8")
        cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)

        minRectangle = mask.copy()
        sub = mask.copy()

        # Erode until the mask fits inside the threshold; stop if it disappears
        while cv2.countNonZero(sub) > 0:
            minRectangle = cv2.erode(minRectangle, None)
            sub = cv2.subtract(minRectangle, thresh_img)

        contours = cv2.findContours(minRectangle.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)

        if len(contours) > 0:
            areaOI = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(areaOI)
        else:
            print("No contours after erosion; falling back to initial bounding box.")

        cv2.imshow("minRectangle Image", minRectangle)
        cv2.waitKey(0)

        # Safe crop using the chosen bounding box
        stitched_crop = stitched_img[y:y+h, x:x+w]
        if stitched_crop.size == 0:
            print("Crop resulted in empty image; saving original stitch instead.")
            stitched_crop = stitched_img

        cv2.imwrite("stitchedOP.png", stitched_crop)
        cv2.imshow("stitched output", stitched_crop)
        cv2.waitKey(0)








