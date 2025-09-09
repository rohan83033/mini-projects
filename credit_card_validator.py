import tkinter as tk
from tkinter import messagebox

def luhn_check(card_number: str) -> bool:
    """Return True if card_number passes Luhn algorithm, else False."""
    card_number = card_number.replace(" ", "")
    if not card_number.isdigit():
        return False
    total = 0
    num_digits = len(card_number)
    parity = num_digits % 2
    for i, digit in enumerate(card_number):
        d = int(digit)
        if i % 2 == parity:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0

def get_card_type(card_number: str) -> str:
    """Detect card type based on number prefixes."""
    card_number = card_number.replace(" ", "")
    if card_number.startswith("4"):
        return "Visa"
    elif card_number.startswith(("51", "52", "53", "54", "55")) or card_number.startswith("2"):
        return "MasterCard"
    elif card_number.startswith(("34", "37")):
        return "American Express"
    elif card_number.startswith("6"):
        return "Discover"
    else:
        return "Unknown"

def validate_card():
    card_num = entry.get().strip()
    if not card_num:
        messagebox.showwarning("Input Error", "Please enter a credit card number.")
        return
    if not card_num.replace(" ", "").isdigit():
        messagebox.showerror("Input Error", "Card number must contain only digits and spaces.")
        return

    card_type = get_card_type(card_num)
    is_valid = luhn_check(card_num)

    if is_valid:
        result_label.config(text=f"Valid {card_type} card number ✔", fg="green")
    else:
        result_label.config(text=f"Invalid {card_type} card number ✘", fg="red")

def clear_input():
    entry.delete(0, tk.END)
    result_label.config(text="")

# Create main window
root = tk.Tk()
root.title("Credit Card Validator")
root.geometry("400x220")
root.resizable(False, False)

# Label
tk.Label(root, text="Enter Credit Card Number:", font=("Arial", 12)).pack(pady=(20, 5))

# Entry field
entry = tk.Entry(root, font=("Arial", 14), width=25)
entry.pack(pady=5)
entry.focus()

# Buttons frame
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

validate_btn = tk.Button(btn_frame, text="Validate", command=validate_card, width=12, bg="#2563eb", fg="white", font=("Arial", 11))
validate_btn.grid(row=0, column=0, padx=5)

clear_btn = tk.Button(btn_frame, text="Clear", command=clear_input, width=12, bg="#6b7280", fg="white", font=("Arial", 11))
clear_btn.grid(row=0, column=1, padx=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Run the app
root.mainloop()
