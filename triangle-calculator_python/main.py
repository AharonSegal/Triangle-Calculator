from gui import TriangleGUI
import tkinter as tk
from math_cal import calculate_triangle
from final_visialization import plot_triangle_sides_angles


def calculate_callback():
    try:
        angle1, angle2, angle3, side1, side2, side3 = triangle_gui.get_input_values()
        result = calculate_triangle(side3, side2, side1, angle1, angle2, angle3,)
        triangle_gui.set_result_label("Triangle calculated successfully!") 
        triangle_gui.set_triangle_data(result)
        plot_triangle_sides_angles(result, "Triangle")

    except (ValueError, AssertionError) as e:
        triangle_gui.set_result_label(str(e))  


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Triangle Calculator")
    triangle_gui = TriangleGUI(window, calculate_callback)
    triangle_gui.run()