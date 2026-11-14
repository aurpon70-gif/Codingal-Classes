import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Length Converter App")  # Title specified in requirements
root.geometry("400x400")           # Window size: width=400, height=400
root.config(bg="#f0f0f0")

# Title label
title_label = tk.Label(root, text="Password Strength Checker", font=("Arial", 14, "bold"), bg="#f0f0f0")
title_label.pack(pady=15)

# Instruction label
instruction_label = tk.Label(root, text="Enter your password below:", font=("Arial", 10), bg="#f0f0f0")
instruction_label.pack(pady=5)

# Password entry box (show='*' hides the password characters for security)
password_entry = tk.Entry(root, show="*", font=("Arial", 12), width=25)
password_entry.pack(pady=10)

# Label to display the result strength
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f0f0f0")
result_label.pack(pady=15)

# Function to check password strength based on the requirements
def check_strength():
    password = password_entry.get()
    length = len(password)
    
    if length <= 5:
        strength = "Weak"
        color = "Red"
    elif 6 <= length <= 8:
        strength = "Medium"
        color = "Yellow"
    elif 9 <= length <= 12:
        strength = "Strong"
        color = "Green"
    else:  # length > 12
        strength = "Very Strong"
        color = "Dark Green"
        
    result_label.config(text=f"Strength: {strength}", fg=color)

# Check button
check_button = tk.Button(root, text="Check Strength", font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", command=check_strength)
check_button.pack(pady=10)

# Run the application
root.mainloop()