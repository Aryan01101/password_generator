import tkinter as tk
from tkinter import ttk
import random
import string
import json
from datetime import datetime

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")
        master.geometry("400x600")

        # Variables
        self.password_var = tk.StringVar()
        self.length_var = tk.IntVar(value=12)
        self.uppercase_var = tk.BooleanVar(value=True)
        self.lowercase_var = tk.BooleanVar(value=True)
        self.numbers_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)

        # Password Length
        ttk.Label(master, text="Password Length:").pack(pady=5)
        length_scale = ttk.Scale(master, from_=6, to=30, variable=self.length_var, orient=tk.HORIZONTAL, length=200, command=self.update_length_label)
        length_scale.pack()
        self.length_label = ttk.Label(master, text="12")
        self.length_label.pack()

        # Checkboxes
        ttk.Checkbutton(master, text="Include Uppercase", variable=self.uppercase_var).pack(pady=5)
        ttk.Checkbutton(master, text="Include Lowercase", variable=self.lowercase_var).pack(pady=5)
        ttk.Checkbutton(master, text="Include Numbers", variable=self.numbers_var).pack(pady=5)
        ttk.Checkbutton(master, text="Include Symbols", variable=self.symbols_var).pack(pady=5)

        # Generate Button
        ttk.Button(master, text="Generate Password", command=self.generate_password).pack(pady=10)

        # Password Display
        ttk.Label(master, text="Generated Password:").pack()
        password_entry = ttk.Entry(master, textvariable=self.password_var, state='readonly', width=30)
        password_entry.pack(pady=5)

        # Save Button
        ttk.Button(master, text="Save Password", command=self.save_password).pack(pady=10)

        # Saved Passwords Display
        ttk.Label(master, text="Saved Passwords:").pack()
        self.saved_passwords_text = tk.Text(master, height=10, width=40)
        self.saved_passwords_text.pack(pady=5)

        self.load_saved_passwords()

    def update_length_label(self, value):
        self.length_label.config(text=str(int(float(value))))

    def generate_password(self):
        length = self.length_var.get()
        chars = ''
        if self.uppercase_var.get():
            chars += string.ascii_uppercase
        if self.lowercase_var.get():
            chars += string.ascii_lowercase
        if self.numbers_var.get():
            chars += string.digits
        if self.symbols_var.get():
            chars += string.punctuation

        if not chars:
            self.password_var.set("Please select at least one option")
            return

        password = ''.join(random.choice(chars) for _ in range(length))
        self.password_var.set(password)

    def save_password(self):
        password = self.password_var.get()
        if password and password != "Please select at least one option":
            saved_passwords = self.load_saved_passwords()
            saved_passwords.append({
                "password": password,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            with open("saved_passwords.json", "w") as f:
                json.dump(saved_passwords, f)
            self.update_saved_passwords_display(saved_passwords)

    def load_saved_passwords(self):
        try:
            with open("saved_passwords.json", "r") as f:
                saved_passwords = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            saved_passwords = []
        self.update_saved_passwords_display(saved_passwords)
        return saved_passwords

    def update_saved_passwords_display(self, saved_passwords):
        self.saved_passwords_text.delete('1.0', tk.END)
        for item in saved_passwords:
            self.saved_passwords_text.insert(tk.END, f"{item['password']} - {item['date']}\n")

root = tk.Tk()
password_generator = PasswordGenerator(root)
root.mainloop()