
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


class RestaurantOrderManagement:

    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management App")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        # Menu items and prices
        self.menu_items = {
            "FRIES MEAL": 2,
            "LUNCH MEAL": 2,
            "BURGER MEAL": 3,
            "PIZZA MEAL": 4,
            "CHEESE BURGER": 2.5,
            "DRINKS": 1
        }

        self.exchange_rate = 82

        # Setup background
        self.setup_background()

        # Main frame
        frame = ttk.Frame(root, padding=15)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Heading
        ttk.Label(
            frame,
            text="Restaurant Order Management",
            font=("Arial", 20, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=15)

        self.menu_labels = {}
        self.menu_quantities = {}

        # Menu items
        for i, (item, price) in enumerate(self.menu_items.items(), start=1):

            label = ttk.Label(
                frame,
                text=f"{item} (${price:.2f}):",
                font=("Arial", 12)
            )
            label.grid(row=i, column=0, padx=10, pady=7, sticky="w")

            self.menu_labels[item] = label

            quantity_entry = ttk.Entry(frame, width=10)
            quantity_entry.grid(row=i, column=1, padx=10, pady=7)

            self.menu_quantities[item] = quantity_entry

        # Currency selection
        self.currency_var = tk.StringVar(value="USD")

        ttk.Label(
            frame,
            text="Currency:",
            font=("Arial", 12)
        ).grid(row=7, column=0, padx=10, pady=10)

        currency_dropdown = ttk.Combobox(
            frame,
            textvariable=self.currency_var,
            state="readonly",
            width=15,
            values=("USD", "INR")
        )

        currency_dropdown.grid(row=7, column=1, padx=10, pady=10)

        self.currency_var.trace_add(
            "write",
            self.update_menu_prices
        )

        # Order button
        ttk.Button(
            frame,
            text="Place Order",
            command=self.place_order
        ).grid(row=8, column=0, columnspan=2, pady=15)

    # Background image
    def setup_background(self):

        try:
            image = Image.open("background.png")
            image = image.resize((800, 600), Image.Resampling.LANCZOS)

            self.background_image = ImageTk.PhotoImage(image)

            background_label = tk.Label(
                self.root,
                image=self.background_image
            )

            background_label.place(x=0, y=0, relwidth=1, relheight=1)

        except FileNotFoundError:

            self.root.configure(bg="lightblue")

            messagebox.showwarning(
                "Background Image",
                "background.png not found. Using plain background."
            )

    # Update menu prices
    def update_menu_prices(self, *args):

        currency = self.currency_var.get()

        symbol = "₹" if currency == "INR" else "$"

        rate = self.exchange_rate if currency == "INR" else 1

        for item, label in self.menu_labels.items():

            price = self.menu_items[item] * rate

            label.config(
                text=f"{item} ({symbol}{price:.2f}):"
            )

    # Place order
    def place_order(self):

        total_cost = 0
        order_summary = "ORDER SUMMARY\n\n"

        currency = self.currency_var.get()

        symbol = "₹" if currency == "INR" else "$"

        rate = self.exchange_rate if currency == "INR" else 1

        order_found = False

        for item, entry in self.menu_quantities.items():

            quantity_text = entry.get().strip()

            if quantity_text == "":
                quantity = 0

            elif not quantity_text.isdigit():

                messagebox.showerror(
                    "Invalid Input",
                    f"Please enter a valid whole-number quantity for {item}."
                )
                entry.focus()
                return

            else:
                quantity = int(quantity_text)

            price = self.menu_items[item] * rate

            cost = quantity * price

            if quantity > 0:

                order_found = True

                total_cost += cost

                order_summary += (
                    f"{item}: {quantity} x {symbol}{price:.2f} "
                    f"= {symbol}{cost:.2f}\n"
                )

        if order_found:

            order_summary += (
                f"\nTotal Cost: {symbol}{total_cost:.2f}"
            )

            messagebox.showinfo(
                "Order Placed Successfully",
                order_summary
            )

        else:

            messagebox.showerror(
                "Error",
                "Please order at least one item."
            )


# Main program
if __name__ == "__main__":

    root = tk.Tk()

    app = RestaurantOrderManagement(root)

    root.mainloop()


        