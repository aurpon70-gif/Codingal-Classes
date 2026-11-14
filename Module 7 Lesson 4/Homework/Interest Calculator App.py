import tkinter as tk
from tkinter import Tk, messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename


def calculate_interest():
  try:
    # Get inputs from the entry fields
    p = float(entry_principal.get())
    t = float(entry_time.get())
    r = float(entry_rate.get())

    # Calculate Simple Interest and Compound Interest
    simple_interest = (p * t * r) / 100
    compound_interest = p * (1 + r / 100) ** t - p

    # Display the results in the labels
    lbl_si_result.config(
        text=f"Simple Interest: {simple_interest:.2f}", fg="blue"
    )
    lbl_ci_result.config(
        text=f"Compound Interest: {compound_interest:.2f}", fg="green"
    )

  except ValueError:
    messagebox.showerror(
        "Invalid Input", "Please enter valid numeric values for all fields."
    )


# Create the main window
root = Tk ()
root.title("Intrest Calculator")
root.geometry("400x400")
root.resizable(False, False)

# Title Label
lbl_title = tk.Label(
    root, text="Interest Calculator", font=("Arial", 16, "bold")
)
lbl_title.pack(pady=10)

# Frame for inputs to keep things organized side-by-side or clean
frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)

# Principal Amount
lbl_principal = tk.Label(
    frame_inputs, text="Principal Amount:", font=("Arial", 10)
)
lbl_principal.grid(row=0, column=0, sticky="w", pady=5)
entry_principal = tk.Entry(frame_inputs, font=("Arial", 10), width=18)
entry_principal.grid(row=0, column=1, pady=5)

# Time Period (Years)
lbl_time = tk.Label(
    frame_inputs, text="Time Period (years):", font=("Arial", 10)
)
lbl_time.grid(row=1, column=0, sticky="w", pady=5)
entry_time = tk.Entry(frame_inputs, font=("Arial", 10), width=18)
entry_time.grid(row=1, column=1, pady=5)

# Rate of Interest (%)
lbl_rate = tk.Label(
    frame_inputs, text="Rate of Interest (%):", font=("Arial", 10)
)
lbl_rate.grid(row=2, column=0, sticky="w", pady=5)
entry_rate = tk.Entry(frame_inputs, font=("Arial", 10), width=18)
entry_rate.grid(row=2, column=1, pady=5)

# Calculate Button
btn_calculate = tk.Button(
    root,
    text="Calculate Interest",
    font=("Arial", 11, "bold"),
    bg="#4CAF50",
    fg="white",
    command=calculate_interest,
)
btn_calculate.pack(pady=15)

# Results Display Labels
lbl_si_result = tk.Label(
    root, text="Simple Interest: ", font=("Arial", 11, "bold")
)
lbl_si_result.pack(pady=5)

lbl_ci_result = tk.Label(
    root, text="Compound Interest: ", font=("Arial", 11, "bold")
)
lbl_ci_result.pack(pady=5)

# Run the application
root.mainloop()