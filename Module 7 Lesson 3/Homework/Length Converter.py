import tkinter as tk
from tkinter import messagebox

# Function to perform the conversion
def convert_length():
    try:
        # Get the value from the entry widget
        inches_value = float(entry_inches.get())
        
        # 1 inch = 2.54 centimeters
        cm_value = inches_value * 2.54
        
        # Display the result
        label_result.config(text=f"{inches_value} inches = {cm_value:.2f} cm")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for inches.")

# Create the main window
root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# Add widgets
title_label = tk.Label(root, text="Length Converter", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333333")
title_label.pack(pady=20)

instruction_label = tk.Label(root, text="Enter length in inches:", font=("Arial", 11), bg="#f0f0f0")
instruction_label.pack(pady=5)

entry_inches = tk.Entry(root, font=("Arial", 12), width=20)
entry_inches.pack(pady=10)

convert_button = tk.Button(root, text="Convert to cm", font=("Arial", 11, "bold"), bg="#ff5722", fg="white", padx=10, pady=5, command=convert_length)
convert_button.pack(pady=15)

label_result = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#009688")
label_result.pack(pady=20)

# Run the application
root.mainloop()