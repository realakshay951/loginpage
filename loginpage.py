import tkinter as tk
from tkinter import messagebox

# Function to validate login credentials
def login():
    username = entry_username.get()
    password = entry_password.get()

    # Predefined username and password
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login Success", "Welcome, you have logged in successfully!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Set up the main window
window = tk.Tk()
window.title("Login Page")
window.geometry("300x200")

# Create and place the widgets (labels, entry fields, and button)
label_username = tk.Label(window, text="Username:")
label_username.pack(pady=5)

entry_username = tk.Entry(window)
entry_username.pack(pady=5)

label_password = tk.Label(window, text="Password:")
label_password.pack(pady=5)

entry_password = tk.Entry(window, show="*")
entry_password.pack(pady=5)

login_button = tk.Button(window, text="Login", command=login)
login_button.pack(pady=20)

# Start the GUI event loop
window.mainloop()
