from PIL import Image

# Open an existing image
image = Image.open('nature.jpeg')

# Display original image
image.show()

# Convert the image to grayscale
gray_image = image.convert('L')
gray_image.show()

# Resize the image
resized_image = image.resize((200, 200))
resized_image.show()

# Rotate the image
rotated_image = image.rotate(45)  # Rotate 45 degrees
rotated_image.show()

# Save the modified images
gray_image.save('gray_example.jpg')
resized_image.save('resized_example.jpg')
rotated_image.save('rotated_example.jpg')

print("Image processing complete. Modified images saved.")
