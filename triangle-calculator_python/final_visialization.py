import matplotlib.pyplot as plt
import numpy as np
from math import degrees

def plot_triangle_sides_angles(result, label):
    angle1 = result[3]
    angle2 = result[4]
    angle3 = result[5]

    side1 = result[0]
    side2 = result[1]
    side3 = result[2]

    area = result[6]
    perimeter = result[7]

    # Calculate the coordinates of the triangle vertices
    A = (0, 0)  # Bottom left
    B = (side1, 0)  # Bottom right
    C_x = side1 - side2 * np.cos(angle3)
    C_y = side2 * np.sin(angle3)
    C = (C_x, C_y)  # Top vertex

    # Plot the triangle
    plt.plot([A[0], B[0]], [A[1], B[1]], 'b-')
    plt.plot([B[0], C[0]], [B[1], C[1]], 'b-')
    plt.plot([C[0], A[0]], [C[1], A[1]], 'b-')
    plt.fill([A[0], B[0], C[0]], [A[1], B[1], C[1]], alpha=0.3, label=label)

    # Convert angles from radians to degrees; round all values
    angle1 = round(degrees(angle1))
    angle2 = round(degrees(angle2))
    angle3 = round(degrees(angle3))
    side1 = round(side1, 2)
    side2 = round(side2, 2)
    side3 = round(side3, 2)

    # Label the sides and angles
    plt.text(B[0] / 2, A[1] - 0.2, f'{side1} cm', fontsize=10)
    plt.text((B[0] + C[0]) / 2, B[1] + 0.2, f'{side2} cm', fontsize=10)
    plt.text(C[0] / 2, (A[1] + C[1]) / 2, f'{side3} cm', fontsize=10)
    plt.text(A[0] - 0.2, A[1] - 0.2, f'{angle2}°', fontsize=10)
    plt.text(B[0] + 0.2, B[1] - 0.2, f'{angle3}°', fontsize=10)
    plt.text(C[0], C[1] + 0.2, f'{angle1}°', fontsize=10)

    plt.axis('equal')
    plt.title(f'{label}\nArea: {area} cm²\nPerimeter: {perimeter} cm')
    plt.show()

