# Anish
# From Internal 2 
# Question 4
# Apply 3D homogenous transformation to scale an object wrt to a pivot point. 
# 5M For the triangle A (3, 2, 2) B (6, 2, 2), C (6, 6, 2), rotate it anti-clockwise 
# direction by 90degree about zaxis keeping A (3, 2,2) fixed. 
# Give the matrices for the original and rotated triangle.

import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def plot_3d_object(vertices, title):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the triangle using Poly3DCollection
    triangle = Poly3DCollection([vertices], color='blue', edgecolors='r')
    ax.add_collection3d(triangle)

    # Set the limits of the plot
    ax.set_xlim([-6, 30])
    ax.set_ylim([-6, 30])
    ax.set_zlim([-6, 30])

    # Set labels for axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Set title
    ax.set_title(title)

    # Display the plot
    plt.show()
    
def rotate_3d_z_axis(vertices, angle_degrees):
    angle_radians = np.radians(angle_degrees)
    rotation_matrix = np.array([[np.cos(angle_radians), -np.sin(angle_radians), -3*np.cos(angle_radians) +2*np.sin(angle_radians)+3],
                                     [np.sin(angle_radians), np.cos(angle_radians), -3*np.sin(angle_radians) -2*np.cos(angle_radians)+2],
                                     [0, 0, 1]])
    rotated_vertices = np.dot(vertices, rotation_matrix)
    return rotated_vertices


def main():
    vertices = np.array([[3, 2, 2],
                          [6, 2, 2],
                          [6, 6, 2],])
    while True:
        print("\nChoose a transformation:")
        print("1. Original")
        print("2. Rotate 90 degree anticlockwise z axis")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            plot_3d_object(vertices, 'Original Triangle')
        elif choice == '2':
            angle = input("Enter rotation angle in degrees keeping A(3,2,2) fixed : ")
            angle_degrees = float(angle)
            vertices = rotate_3d_z_axis(vertices,angle_degrees)
            print(vertices)
            plot_3d_object(vertices, 'Transformed Triangle by ')
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

    print("Exiting...")

if __name__ == "__main__":
    main()
