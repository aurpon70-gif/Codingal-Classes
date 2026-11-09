from datetime import date
from tkinter import Tk, Label, Entry, Button, END, StringVar


def calculate_age():
  try:
    # Get user inputs
    name = name_entry.get()
    d = int(date_entry.get())
    m = int(month_entry.get())
    y = int(year_entry.get())

    # Get current date
    today = date.today()

    # Calculate age
    age_years = today.year - y
    age_months = today.month - m
    age_days = today.day - d

    # Adjust if birth day/month hasn't occurred yet this year
    if age_days < 0:
      age_months -= 1
      # Approximate days in previous month or simplify
      age_days += 30
    if age_months < 0:
      age_years -= 1
      age_months += 1

    # Display personalized message
    result_text.set(
        f"Hello {name}! You are {age_years} years, "
        f"{age_months} months, and {age_days} days old."
    )
  except ValueError:
    result_text.set("Please enter valid numeric values for date, month, & year.")


# Create the main window
root = Tk()
root.geometry("400x400")
root.title("Age Calculator App")
root.config(bg="#f0f0f0")

# Heading
title_label = Label(
    root,
    text="Age Calculator",
    font=("Arial", 16, "bold"),
    bg="#f0f0f0",
    fg="#333333",
)
title_label.pack(pady=15)

# --- Form Frame for Side-by-Side Widgets ---
form_frame = Label(root, bg="#f0f0f0")
form_frame.pack(pady=10)

# 1. Name Input
Label(
    form_frame,
    text="Name:",
    font=("Arial", 11),
    bg="#f0f0f0",
    anchor="w",
    width=10,
).grid(row=0, column=0, padx=5, pady=8, sticky="w")
name_entry = Entry(form_frame, font=("Arial", 11), width=20)
name_entry.grid(row=0, column=1, padx=5, pady=8)

# 2. Date Input
Label(
    form_frame,
    text="Date (DD):",
    font=("Arial", 11),
    bg="#f0f0f0",
    anchor="w",
    width=10,
).grid(row=1, column=0, padx=5, pady=8, sticky="w")
date_entry = Entry(form_frame, font=("Arial", 11), width=20)
date_entry.grid(row=1, column=1, padx=5, pady=8)

# 3. Month Input
Label(
    form_frame,
    text="Month (MM):",
    font=("Arial", 11),
    bg="#f0f0f0",
    anchor="w",
    width=10,
).grid(row=2, column=0, padx=5, pady=8, sticky="w")
month_entry = Entry(form_frame, font=("Arial", 11), width=20)
month_entry.grid(row=2, column=1, padx=5, pady=8)

# 4. Year Input
Label(
    form_frame,
    text="Year (YYYY):",
    font=("Arial", 11),
    bg="#f0f0f0",
    anchor="w",
    width=10,
).grid(row=3, column=0, padx=5, pady=8, sticky="w")
year_entry = Entry(form_frame, font=("Arial", 11), width=20)
year_entry.grid(row=3, column=1, padx=5, pady=8)

# Calculate Button
calc_button = Button(
    root,
    text="Calculate Age",
    font=("Arial", 11, "bold"),
    bg="#ff5722",
    fg="white",
    command=calculate_age,
)
calc_button.pack(pady=15)

# Result Message Display
result_text = StringVar()
result_label = Label(
    root,
    textvariable=result_text,
    font=("Arial", 10, "italic"),
    bg="#f0f0f0",
    fg="#00796b",
    wraplength=350,
)
result_label.pack(pady=10)

# Run the application
root.mainloop()