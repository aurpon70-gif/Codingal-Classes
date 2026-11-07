import tkinter as tk

# 1. Initialize the main window
root = tk.Tk()

# 2. Set the window title and size (width = 400, height = 300)
root.title("Getting Started with Widgets")
root.geometry("400x300")

# 3. Add a label to describe the functionality of this application
desc_label = tk.Label(root, text="This application calculates the product of two numbers.", font=("Arial", 10))
desc_label.pack(pady=5)

# 4. Add two labels for asking users to enter numbers in the respective text box
label1 = tk.Label(root, text="Enter first number:")
label1.pack(anchor="w", padx=40)

# 5. Add two Entry widgets below the last two mentioned labels to get the numbers
entry1 = tk.Entry(root)
entry1.pack(pady=2)

label2 = tk.Label(root, text="Enter second number:")
label2.pack(anchor="w", padx=40)

entry2 = tk.Entry(root)
entry2.pack(pady=2)

# Function to calculate the product
def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        # 7. Display the result in the Text Box
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, f"The product is: {result}")
    except ValueError:
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, "Please enter valid numbers.")

# 6. Add a button that will calculate the product when it is clicked
calc_button = tk.Button(root, text="Calculate Product", command=calculate_product)
calc_button.pack(pady=8)

# 7. Add a Text Box to display the result
text_box = tk.Text(root, height=3, width=30)
text_box.pack(pady=5)

# Run the application
root.mainloop()