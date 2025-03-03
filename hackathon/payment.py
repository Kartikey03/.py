import tkinter as tk
from tkinter import messagebox

def process_payment():
    card_number = card_number_entry.get()
    card_holder = card_holder_entry.get()
    cvv = cvv_entry.get()
    amount = amount_entry.get()

    # Perform validation checks
    if len(card_number) != 12:
        messagebox.showerror("Error", "Invalid card number. Card number must be 12 digits.")
        return

    if len(cvv) != 3:
        messagebox.showerror("Error", "Invalid CVV. CVV must be 3 digits.")
        return
    
    if card_holder == "":
        messagebox.showerror("Error", "Card Holder Name cannot be Empty.")
        return
    
    if amount == "":
        messagebox.showerror("Error", "Amount cannot be Empty.")
        return
    
    if card_number == "":
        messagebox.showerror("Error", "Card Number cannot be Empty.")
        return
    
    if cvv == "":
        messagebox.showerror("Error", "CVV cannot be Empty.")
        return

    # Here, you can implement the logic to interact with a real payment gateway
    # and process the payment.

    messagebox.showinfo("Payment Confirmation", "Payment Successful!")

def create_payment_form():
    window = tk.Tk()
    window.title("Payment Gateway")

    global card_number_entry, card_holder_entry, cvv_entry, amount_entry 

    card_number_label = tk.Label(window, text="Card Number:")
    card_number_label.pack()
    card_number_entry = tk.Entry(window)
    card_number_entry.pack()

    card_holder_label = tk.Label(window, text="Card Holder:")
    card_holder_label.pack()
    card_holder_entry = tk.Entry(window)
    card_holder_entry.pack()

    cvv_label = tk.Label(window, text="CVV:")
    cvv_label.pack()
    cvv_entry = tk.Entry(window)
    cvv_entry.pack()

    amount_label = tk.Label(window, text="Amount:")
    amount_label.pack()
    amount_entry = tk.Entry(window)
    amount_entry.pack()

    process_button = tk.Button(window, text="Process Payment", command=process_payment)
    process_button.pack()

    window.mainloop()

# Create the payment form
create_payment_form()
