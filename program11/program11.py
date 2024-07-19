import cv2

# Read the image
image = cv2.imread('nature.jpeg', 1)

# Split the image into its color channels
B, G, R = cv2.split(image)

# Display the original image
cv2.imshow('Original Image', image)
cv2.waitKey(0)

# Display the blue channel
cv2.imshow('Blue Channel', B)
cv2.waitKey(0)

# Display the green channel
cv2.imshow('Green Channel', G)
cv2.waitKey(0)

# Display the red channel
cv2.imshow('Red Channel', R)
cv2.waitKey(0)

# Close all the windows
cv2.destroyAllWindows()
