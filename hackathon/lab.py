import mysql.connector
from tkinter import *
from tkinter import messagebox

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@kiman2003",
    database="login"
)

# Create the 'users' table if it doesn't exist
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255), type INT)")


def register_user():
    username = register_username.get()
    password = register_password.get()
    user_type = 1  # Assuming user type 1 for patients

    # Check if the user already exists
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    if cursor.fetchone():
        messagebox.showerror("Registration Error", "Username already exists. Please choose a different username.")
    else:
        # Insert the user into the database
        cursor.execute("INSERT INTO users (username, password, type) VALUES (%s, %s, %s)", (username, password, user_type))
        db.commit()
        messagebox.showinfo("Registration Success", "Registration successful.")


def login_user():
    username = login_username.get()
    password = login_password.get()

    # Check if the username and password match
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    if user:
        messagebox.showinfo("Login Success", "Login successful.")
        user_type = user[3]  # Return the user type

        if user_type == 1:
            print("Logged in as a patient.")
            # Perform patient-specific actions
        else:
            print("Invalid user type.")
    else:
        messagebox.showerror("Login Error", "Invalid username or password.")


# Create the main window
window = Tk()
window.title("Pathology Management Login")
window.geometry("350x350")

# Create labels and entry fields for registration
register_label = Label(window, text="Registration")
register_label.pack()

register_username_label = Label(window, text="Username:")
register_username_label.pack()

register_username = Entry(window)
register_username.pack()

register_password_label = Label(window, text="Password:")
register_password_label.pack()

register_password = Entry(window, show="*")
register_password.pack()

register_button = Button(window, text="Register", command=register_user)
register_button.pack()

# Create labels and entry fields for login
login_label = Label(window, text="Login")
login_label.pack()

login_username_label = Label(window, text="Username:")
login_username_label.pack()

login_username = Entry(window)
login_username.pack()

login_password_label = Label(window, text="Password:")
login_password_label.pack()

login_password = Entry(window, show="*")
login_password.pack()

login_button = Button(window, text="Login", command=login_user)
login_button.pack()

# Start the main event loop
window.mainloop()

# Close the database connection
db.close()
