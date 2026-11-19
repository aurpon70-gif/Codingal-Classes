import random
import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.geometry("400x400")
root.title("Rock Paper Scissor")
root.resizable(False, False)

# Heading Label
title_label = tk.Label(
    root, text="Rock Paper Scissor", font=("Arial", 18, "bold")
)
title_label.pack(pady=15)

# Result Display Labels
result_label = tk.Label(
    root, text="Let's Play!", font=("Arial", 14), fg="blue"
)
result_label.pack(pady=10)

choice_label = tk.Label(root, text="", font=("Arial", 12))
choice_label.pack(pady=5)


# Game Logic Function
def play(user_choice):
  options = ["Rock", "Paper", "Scissors"]
  computer_choice = random.choice(options)

  # Determine the winner
  if user_choice == computer_choice:
    result = "It's a Tie!"
  elif (
      (user_choice == "Rock" and computer_choice == "Scissors")
      or (user_choice == "Paper" and computer_choice == "Rock")
      or (user_choice == "Scissors" and computer_choice == "Paper")
  ):
    result = "You Win! 🎉"
  else:
    result = "Computer Wins! 💻"

  # Update labels with choices and result
  choice_label.config(
      text=f"Your Choice: {user_choice}\nComputer's Choice: {computer_choice}"
  )
  result_label.config(text=result)


# Buttons for User Choices
btn_frame = tk.Frame(root)
btn_frame.pack(pady=20)

rock_btn = tk.Button(
    btn_frame,
    text="Rock",
    font=("Arial", 12),
    width=8,
    command=lambda: play("Rock"),
)
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(
    btn_frame,
    text="Paper",
    font=("Arial", 12),
    width=8,
    command=lambda: play("Paper"),
)
paper_btn.grid(row=0, column=1, padx=5)

scissor_btn = tk.Button(
    btn_frame,
    text="Scissors",
    font=("Arial", 12),
    width=8,
    command=lambda: play("Scissors"),
)
scissor_btn.grid(row=0, column=2, padx=5)

# Run the application
root.mainloop()