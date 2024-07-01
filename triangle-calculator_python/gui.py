import tkinter as tk
import math

class TriangleGUI:
    def __init__(self, window, calculate_callback):
        self.window = window
        self.calculate_callback = calculate_callback
        self.create_gui()

    def create_gui(self):
        # Create the GUI elements (canvas, entry fields, labels, buttons)
        self.canvas = tk.Canvas(self.window, width=800, height=800)
        self.canvas.pack()

        # Draw the triangle on the canvas
        self.canvas.create_polygon(200, 600, 600, 600, 400, 200, fill="white", outline="black")

        # Create the input fields and labels on the triangle
        self.angle1_entry = self.create_entry(300, 560, "Angle 1")
        self.angle1_label = self.create_label(300, 620)

        self.angle2_entry = self.create_entry(500, 560, "Angle 2")
        self.angle2_label = self.create_label(500, 620)

        self.angle3_entry = self.create_entry(400, 240, "Angle 3")
        self.angle3_label = self.create_label(400, 300)

        self.side1_entry = self.create_entry(400, 560, "Side 1")
        self.side1_label = self.create_label(400, 620)

        self.side2_entry = self.create_entry(260, 400, "Side 2")
        self.side2_label = self.create_label(260, 460)

        self.side3_entry = self.create_entry(540, 400, "Side 3")
        self.side3_label = self.create_label(540, 460)

        # Create the buttons
        self.calculate_button = tk.Button(self.window, text="Calculate", command=self.calculate_callback, font=("Arial", 14))
        self.canvas.create_window(400, 100, window=self.calculate_button)

        self.clear_button = tk.Button(self.window, text="Clear", command=self.clear_entries, font=("Arial", 14))
        self.canvas.create_window(300, 100, window=self.clear_button)

        self.restart_button = tk.Button(self.window, text="Restart", command=self.restart_calculator, font=("Arial", 14))
        self.canvas.create_window(500, 100, window=self.restart_button)

        self.result_label = tk.Label(self.window, text="", font=("Arial", 14))
        self.canvas.create_window(400, 50, window=self.result_label)

        # Display requirements
        requirements_text = "Requirements:\n" \
                            "- Two angles and one side\n" \
                            "- Two sides and one angle\n" \
                            "- Three angles"
                            # "note: 'side-side-angle' is the situation when you give two sides and an angle which is not between them\n" \
                            # "This is usually not enough information to specify a unique triangle."

    
        self.requirements_label = tk.Label(self.window, text=requirements_text, font=("Arial", 12), justify=tk.LEFT)
        self.canvas.create_window(100, 200, window=self.requirements_label, anchor=tk.NW)

    def create_entry(self, x, y, default_text):
        entry = tk.Entry(self.window, width=10, fg='gray')
        entry.default_text = default_text
        entry.insert(0, default_text)
        entry.bind('<FocusIn>', self.on_entry_click)
        entry.bind('<FocusOut>', self.on_focusout)
        self.canvas.create_window(x, y, window=entry)
        return entry

    def create_label(self, x, y):
        label = tk.Label(self.window, text="", font=("Arial", 12))
        self.canvas.create_window(x, y, window=label)
        return label

    def on_entry_click(self, event):
        if event.widget.get() == event.widget.default_text:
            event.widget.delete(0, tk.END)
            event.widget.config(fg='black')

    def on_focusout(self, event):
        if event.widget.get() == "":
            event.widget.insert(0, event.widget.default_text)
            event.widget.config(fg='gray')

    def get_input_values(self):
        #get angle inputs as radiens
        angle1 = math.radians(float(self.angle1_entry.get())) if self.angle1_entry.get() != self.angle1_entry.default_text else None
        angle2 = math.radians(float(self.angle2_entry.get())) if self.angle2_entry.get() != self.angle2_entry.default_text else None
        angle3 = math.radians(float(self.angle3_entry.get())) if self.angle3_entry.get() != self.angle3_entry.default_text else None
        side1 = float(self.side1_entry.get()) if self.side1_entry.get() != self.side1_entry.default_text else None
        side2 = float(self.side2_entry.get()) if self.side2_entry.get() != self.side2_entry.default_text else None
        side3 = float(self.side3_entry.get()) if self.side3_entry.get() != self.side3_entry.default_text else None
        return angle1, angle2, angle3, side1, side2, side3
    
    def update_labels(self, angle1, angle2, angle3, side1, side2, side3):
        self.angle1_label.config(text="{:.2f}°".format(angle1))
        self.angle2_label.config(text="{:.2f}°".format(angle2))
        self.angle3_label.config(text="{:.2f}°".format(angle3))
        self.side1_label.config(text="{:.2f}".format(side1))
        self.side2_label.config(text="{:.2f}".format(side2))
        self.side3_label.config(text="{:.2f}".format(side3))


    def clear_entries(self):
        self.angle1_entry.delete(0, tk.END)
        self.angle1_entry.insert(0, self.angle1_entry.default_text)
        self.angle1_entry.config(fg='gray')

        self.angle2_entry.delete(0, tk.END)
        self.angle2_entry.insert(0, self.angle2_entry.default_text)
        self.angle2_entry.config(fg='gray')

        self.angle3_entry.delete(0, tk.END)
        self.angle3_entry.insert(0, self.angle3_entry.default_text)
        self.angle3_entry.config(fg='gray')

        self.side1_entry.delete(0, tk.END)
        self.side1_entry.insert(0, self.side1_entry.default_text)
        self.side1_entry.config(fg='gray')

        self.side2_entry.delete(0, tk.END)
        self.side2_entry.insert(0, self.side2_entry.default_text)
        self.side2_entry.config(fg='gray')

        self.side3_entry.delete(0, tk.END)
        self.side3_entry.insert(0, self.side3_entry.default_text)
        self.side3_entry.config(fg='gray')

        self.result_label.config(text="")

    def restart_calculator(self):
        self.clear_entries()
        self.angle1_label.config(text="")
        self.angle2_label.config(text="")
        self.angle3_label.config(text="")
        self.side1_label.config(text="")
        self.side2_label.config(text="")
        self.side3_label.config(text="")

    def set_result_label(self, text):
        self.result_label.config(text=text, fg='black')

    def set_triangle_data(self, result):
        # Unpack the result tuple
        side3, side2, side1, angle1, angle2, angle3, area, perimeter = result
        
        # Convert angles from radians to degrees
        angle1 = math.degrees(angle1)
        angle2 = math.degrees(angle2)
        angle3 = math.degrees(angle3)
        
        # Update the labels with the values
        self.angle1_label.config(text=f"{angle1:.2f}°")
        self.angle2_label.config(text=f"{angle2:.2f}°")
        self.angle3_label.config(text=f"{angle3:.2f}°")
        self.side1_label.config(text=f"{side1:.2f} cm")
        self.side2_label.config(text=f"{side2:.2f} cm")
        self.side3_label.config(text=f"{side3:.2f} cm")
        
        # Display area and perimeter
        self.result_label.config(text=f"Area: {area:.2f} cm², Perimeter: {perimeter:.2f} cm")


    def run(self):
        self.window.mainloop()