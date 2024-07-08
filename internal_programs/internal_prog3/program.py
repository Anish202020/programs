import cv2
import matplotlib.pyplot as plt

# Function to split the image into quadrants
def split_image(image):
    # Get the dimensions of the image
    height, width = image.shape[:2]

    # Calculate the center points
    center_x, center_y = width // 2, height // 2

    # Split the image into quadrants
    top_left = image[:center_y, :center_x]
    top_right = image[:center_y, center_x:]
    bottom_left = image[center_y:, :center_x]
    bottom_right = image[center_y:, center_x:]

    return top_left, top_right, bottom_left, bottom_right

# Function to display the quadrants
def display_quadrants(tl, tr, bl, br):
    # Create a figure to display the quadrants
    plt.figure(figsize=(10, 10))

    # Display top-left quadrant
    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(tl, cv2.COLOR_BGR2RGB))
    plt.title('Top Left')

    # Display top-right quadrant
    plt.subplot(2, 2, 2)
    plt.imshow(cv2.cvtColor(tr, cv2.COLOR_BGR2RGB))
    plt.title('Top Right')

    # Display bottom-left quadrant
    plt.subplot(2, 2, 3)
    plt.imshow(cv2.cvtColor(bl, cv2.COLOR_BGR2RGB))
    plt.title('Bottom Left')

    # Display bottom-right quadrant
    plt.subplot(2, 2, 4)
    plt.imshow(cv2.cvtColor(br, cv2.COLOR_BGR2RGB))
    plt.title('Bottom Right')

    plt.show()

# Main function
def main():
    # Read the image
    image_path = 'neutrality.jpg'  # Replace with your image path
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Unable to read the image file.")
        return

    # Split the image into quadrants
    top_left, top_right, bottom_left, bottom_right = split_image(image)

    # Display the quadrants
    display_quadrants(top_left, top_right, bottom_left, bottom_right)

if __name__ == "__main__":
    main()