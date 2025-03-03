import tkinter as tk
import webbrowser
from datetime import date


class Patient:
    def __init__(self, name, age, blood_group, tests):
        self.name = name
        self.age = age
        self.blood_group = blood_group
        self.tests = tests


def generate_receipt(patient):
    receipt_content = f"Name: {patient.name}\nAge: {patient.age}\nBlood Group: {patient.blood_group}\nDate: {date.today().strftime('%d/%m/%Y')}\n\n"
    receipt_content += "Test Name\t\tPrice\n"
    receipt_content += "--------------------------------\n"

    total_amount = 0
    for test_name, test_price in patient.tests.items():
        receipt_content += f"{test_name}\t\t{test_price}\n"
        total_amount += test_price

    receipt_content += "--------------------------------\n"
    receipt_content += f"Total Amount:\t\t{total_amount}\n"

    return receipt_content


def print_receipt(patient):
    receipt_content = generate_receipt(patient)
    
    # Create an HTML file with the receipt content
    html_content = f"<pre>{receipt_content}</pre>"
    with open("receipt.html", "w") as file:
        file.write(html_content)

    # Open the HTML file in a web browser
    webbrowser.open("receipt.html")


def show_receipt(patient):
    receipt_content = generate_receipt(patient)

    window = tk.Tk()
    window.title("Bill Receipt")

    receipt_text = tk.Text(window, height=10, width=40, font=("Courier New", 12), bd=0, bg="#F0F0F0", padx=10, pady=10)
    receipt_text.insert(tk.END, receipt_content)
    receipt_text.configure(state="disabled")
    receipt_text.pack()

    total_label = tk.Label(window, text=f"Total Amount: {sum(patient.tests.values()):.2f}", font=("Arial", 12, "bold"))
    total_label.pack(pady=10)

    print_button = tk.Button(window, text="Print", command=lambda: print_receipt(patient), font=("Arial", 12, "bold"))
    print_button.pack(pady=10)

    window.mainloop()


# Example usage
patient = Patient("John Doe", 30, "AB+", {"Blood Test": 150.00, "Urine Test": 100.00, "X-ray": 200.00})
show_receipt(patient)
