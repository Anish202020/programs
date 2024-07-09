import cv2
import numpy as np

# Function to translate the image
def translate_image(image, dx, dy):
    rows, cols = image.shape[:2]
    translation_matrix = np.float32([[1, 0, dx], [0, 1, dy]])
    translated_image = cv2.warpAffine(image, translation_matrix, (cols, rows))
    return translated_image

# Read the image
image = cv2.imread('neutrality.jpg')
if image is None:
    print("Error: Image not found.")
    exit()

# Get image dimensions
height, width = image.shape[:2]

# Calculate the center coordinates of the image
center = (width // 2, height // 2)

# Get user inputs for rotation, scaling, and translation
rotation_value = float(input("Enter the degree of Rotation: "))
scaling_value = float(input("Enter the zooming factor: "))
h = int(input("How many pixels you want the image to be translated horizontally? "))
v = int(input("How many pixels you want the image to be translated vertically? "))

# Create the 2D rotation matrix for rotation
rotation_matrix = cv2.getRotationMatrix2D(center=center, angle=rotation_value, scale=1)
# Apply the rotation to the image
rotated_image = cv2.warpAffine(src=image, M=rotation_matrix, dsize=(width, height))

# Create the 2D rotation matrix for scaling (angle=0 for scaling only)
scaling_matrix = cv2.getRotationMatrix2D(center=center, angle=0, scale=scaling_value)
# Apply the scaling to the rotated image
scaled_image = cv2.warpAffine(src=rotated_image, M=scaling_matrix, dsize=(width, height))

# Apply the translation to the scaled image
translated_image = translate_image(scaled_image, dx=h, dy=v)

# Display the images
cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)
cv2.imshow('Scaled Image', scaled_image)
cv2.imshow('Translated Image', translated_image)

# Wait for a key press and close the image windows
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the final image
cv2.imwrite('Final_image.png', translated_image)
print("Final image saved as 'Final_image.png'")
