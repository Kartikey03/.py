import tkinter as tk
import webbrowser


class Patient:
    def __init__(self, name, age, test_name, amount, blood_group, address, gender, payment_status):
        self.name = name
        self.age = age
        self.test_name = test_name
        self.amount = amount
        self.blood_group = blood_group
        self.address = address
        self.gender = gender
        self.payment_status = payment_status


def generate_receipt(patient):
    receipt_content = f"Name: {patient.name}\nAge: {patient.age}\nTest Name: {patient.test_name}\nAmount: {patient.amount}\n"
    receipt_content += f"Blood Group: {patient.blood_group}\nAddress: {patient.address}\nGender: {patient.gender}\nPayment Status: {patient.payment_status}\n"
    return receipt_content


def print_receipt(patient):
    receipt_content = generate_receipt(patient)

    # Create an HTML file for the receipt
    html_content = f"""
    <html>
    <head>
        <title>Bill Receipt</title>
        <style>
        h1 {{
            color: #333333;
            text-align: center;
        }}
        pre {{
            font-family: 'Courier New', Courier, monospace;
            font-size: 12pt;
            background-color: #F0F0F0;
            padding: 10px;
        }}
        </style>
    </head>
    <body>
        <h1>Patient Bill</h1>
        <pre>{receipt_content}</pre>
    </body>
    </html>
    """

    # Create a temporary HTML file
    with open("receipt.html", "w") as file:
        file.write(html_content)

    # Open the HTML file in the default web browser
    webbrowser.open("receipt.html")


def show_receipt(patient):
    receipt_content = generate_receipt(patient)

    # Create a Tkinter window
    window = tk.Tk()
    window.title("Bill Receipt")

    # Create a Label for the heading
    heading_label = tk.Label(window, text="Patient Bill", font=("Arial", 16, "bold"), pady=10)
    heading_label.pack()

    # Create a Text widget to display the receipt content
    receipt_text = tk.Text(window, height=10, width=40, font=("Courier New", 12), bd=0, bg="#F0F0F0", padx=10, pady=10)
    receipt_text.insert(tk.END, receipt_content)
    receipt_text.configure(state="disabled")
    receipt_text.pack()

    # Create a Print button
    print_button = tk.Button(window, text="Print", command=lambda: print_receipt(patient), font=("Arial", 12, "bold"))
    print_button.pack(pady=10)

    # Run the Tkinter event loop
    window.mainloop()


# Example usage
patient = Patient("John Doe", 30, "Blood Test", 150.00, "AB+", "123 Main St", "Male", "Paid")
show_receipt(patient)
