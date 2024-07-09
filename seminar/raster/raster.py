from PIL import Image
import matplotlib.pyplot as plt

# Open an existing image
image = Image.open('nature.jpeg')

# Convert the image to grayscale
gray_image = image.convert('L')

# Resize the image
resized_image = image.resize((200, 200))

# Rotate the image
rotated_image = image.rotate(45)  # Rotate 45 degrees

# Prepare a list of images to display
images = [image, gray_image, resized_image, rotated_image]
titles = ["Original", "Grayscale", "Resized", "Rotated"]

# Set up the plot
fig, axes = plt.subplots(1, 4, figsize=(20, 5))

for ax, img, title in zip(axes, images, titles):
    ax.imshow(img, cmap='gray' if img.mode == 'L' else None)
    ax.set_title(title)
    ax.axis('off')

plt.tight_layout()
plt.show()

# Save the modified images
gray_image.save('gray_example.jpg')
resized_image.save('resized_example.jpg')
rotated_image.save('rotated_example.jpg')

print("Image processing complete. Modified images saved.")
