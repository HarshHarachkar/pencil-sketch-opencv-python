import cv2

# Read the image
image = cv2.imread('Lofi.webp')

# Convert to gray scale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
inverted_image = cv2.bitwise_not(gray_image)

# Blur the inverted image
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

# Invert the blurred image
inverted_blurred = cv2.bitwise_not(blurred)

# Create the pencil sketch image
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

# Display the original and sketch images
cv2.imshow('Original Image', image)
cv2.imshow('Pencil Sketch', pencil_sketch)

# Save the sketch image
cv2.imwrite('pencil_sketch.jpg', pencil_sketch)

cv2.waitKey(0)
cv2.destroyAllWindows()
