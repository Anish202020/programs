# From Internal 2 
# Question 7
# Apply appropriate algorithm to draw a 3D unit cube at origin, rotate it by 45
# degrees on z-axis. Translate the original polygon (without rotation) by 10
# Units on x axis and scale by a factor of (2,2, 3). Give the matrices
# forthe original and transformed 3d cube.

import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def plot_3d_object(vertices, title):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title(title)

    # Plot the 3D object
    for i in range(len(vertices)):
        ax.scatter(vertices[i, 0], vertices[i, 1], vertices[i, 2], color='b')
        ax.text(vertices[i, 0], vertices[i, 1], vertices[i, 2], f'P{i}', ha='right')

    # Connect vertices to form edges of the object
    edges = [[0, 1, 2, 3, 0],
             [4, 5, 6, 7, 4],
             [0, 4], [1, 5], [2, 6], [3, 7]]
    for edge in edges:
        ax.plot(vertices[edge, 0], vertices[edge, 1], vertices[edge, 2], 'b-')

    plt.show()

# Translated
def translate_3d_object(vertices):
    translated_vertices = vertices + np.array([10, 0, 0])
    print(translated_vertices)
    return translated_vertices

# Rotated by 45 
def rotate_3d_z_axis(vertices,angle_degrees):
    angle_radians = np.radians(angle_degrees)
    rotation_matrix = np.array([[np.cos(angle_radians), -np.sin(angle_radians), 0],
                                     [np.sin(angle_radians), np.cos(angle_radians),0],
                                     [0, 0, 1]])
    rotated_vertices = np.dot(vertices, rotation_matrix)
    return rotated_vertices
    
# Scaled by (2,2,3)
def scale_3d_object(vertices):
    scaled_vertices = vertices * np.array([2, 2, 3])
    return scaled_vertices    
def main():
    vertices = np.array([[0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1]])
    while True:
        print("\nChoose a transformation:")
        print("1. Original")
        print("2. Rotate 45 degree anticlockwise z axis")
        print("3. Translate and Scale")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            plot_3d_object(vertices, 'Original Cube')
        elif choice == '2':
            angle = "45"
            angle_degrees = float(angle)
            vertices = rotate_3d_z_axis(vertices,angle_degrees)
            
            plot_3d_object(vertices, 'Transformed Triangle by '+angle +" degrees")
        elif choice == '3':
            vertices = translate_3d_object(vertices)
            plot_3d_object(vertices, 'Translated Cube')
            
            vertices = scale_3d_object(vertices)
            plot_3d_object(vertices, 'Scaled Cube')
            
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

    print("Exiting...")

if __name__ == "__main__":
    main()
