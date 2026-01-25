from PIL import Image

# Open image
img = Image.open("input.jpg")

# Manual size (width, height)
new_size = (300, 200)

# Resize
resized_img = img.resize(new_size)

# Save image
resized_img.save("output.jpg")

print("Image resized successfully")
