import numpy as np
import cv2

# Read image in grayscale
img = cv2.imread("image.png", cv2.IMREAD_GRAYSCALE)

h, w = img.shape

# Scaling factors
sx = 2.0   # scale width
sy = 2.0   # scale height

# New image size
new_h = int(h * sy)
new_w = int(w * sx)

# Create empty output image
scaled_img = np.zeros((new_h, new_w), dtype=np.uint8)

# Nearest Neighbor Scaling
for y in range(new_h):
    for x in range(new_w):
        orig_x = int(x / sx)
        orig_y = int(y / sy)

        if orig_x < w and orig_y < h:
            scaled_img[y, x] = img[orig_y, orig_x]

# Display
cv2.imshow("Original", img)
cv2.imshow("Scaled", scaled_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
