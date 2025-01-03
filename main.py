import tkinter as tk
from tkinter import messagebox
import hashlib
import os
import datetime

# Helper Functions
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def save_account(account_number, name, hashed_password, balance):
    with open("accounts.txt", "a") as f:
        f.write(f"{account_number},{name},{hashed_password},{balance}\n")

def load_accounts():
    accounts = {}
    if os.path.exists("accounts.txt"):
        with open("accounts.txt", "r") as f:
            for line in f:
                account_number, name, hashed_password, balance = line.strip().split(",")
                accounts[account_number] = {
                    "name": name,
                    "password": hashed_password,
                    "balance": float(balance),
                }
    return accounts

def log_transaction(account_number, transaction_type, amount, status, balance):
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    with open("transactions.txt", "a") as f:
        f.write(f"{account_number},{transaction_type},{amount},{status},{balance},{date}\n")

def load_transactions(account_number):
    transactions = []
    if os.path.exists("transactions.txt"):
        with open("transactions.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 6:  # Ensure the line has exactly 6 values
                    acc_num, transaction_type, amount, status, balance, date = parts
                    if acc_num == account_number:
                        transactions.append((transaction_type, amount, status, balance, date))
                else:
                    print(f"Malformed transaction line: {line.strip()}")  # Debug log
    return transactions


class BankingSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Banking System")
        self.root.geometry("400x400")

        self.main_menu()

    def main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Welcome to the Banking System!", font=("Arial", 16)).pack(pady=20)
        tk.Button(self.root, text="Create Account", command=self.create_account_screen, width=20).pack(pady=10)
        tk.Button(self.root, text="Login", command=self.login_screen, width=20).pack(pady=10)
        tk.Button(self.root, text="Forgot Password", command=self.forgot_password_screen, width=20).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit, width=20).pack(pady=10)

    def create_account_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Create Account", font=("Arial", 16)).pack(pady=20)
        
        tk.Label(self.root, text="Name:").pack()
        name_entry = tk.Entry(self.root)
        name_entry.pack()

        tk.Label(self.root, text="Initial Deposit:").pack()
        deposit_entry = tk.Entry(self.root)
        deposit_entry.pack()

        tk.Label(self.root, text="Password:").pack()
        password_entry = tk.Entry(self.root, show="*")
        password_entry.pack()

        def create_account():
            name = name_entry.get()
            try:
                initial_deposit = float(deposit_entry.get())
                account_number = str(len(load_accounts()) + 1).zfill(6)
                hashed_password = hash_password(password_entry.get())

                save_account(account_number, name, hashed_password, initial_deposit)
                messagebox.showinfo("Success", f"Account created successfully!\nYour account number: {account_number}")
                self.main_menu()
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid deposit amount.")

        tk.Button(self.root, text="Create", command=create_account).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=10)

    def login_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Login", font=("Arial", 16)).pack(pady=20)
        
        tk.Label(self.root, text="Account Number:").pack()
        account_entry = tk.Entry(self.root)
        account_entry.pack()

        tk.Label(self.root, text="Password:").pack()
        password_entry = tk.Entry(self.root, show="*")
        password_entry.pack()

        def login():
            accounts = load_accounts()
            account_number = account_entry.get()
            password = password_entry.get()

            if account_number in accounts and accounts[account_number]["password"] == hash_password(password):
                messagebox.showinfo("Success", "Login successful!")
                self.account_menu(account_number)
            else:
                messagebox.showerror("Error", "Invalid account number or password.")

        tk.Button(self.root, text="Login", command=login).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=10)

    def forgot_password_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Forgot Password", font=("Arial", 16)).pack(pady=20)
        
        tk.Label(self.root, text="Account Number:").pack()
        account_entry = tk.Entry(self.root)
        account_entry.pack()

        tk.Label(self.root, text="New Password:").pack()
        new_password_entry = tk.Entry(self.root, show="*")
        new_password_entry.pack()

        def reset_password():
            accounts = load_accounts()
            account_number = account_entry.get()
            new_password = new_password_entry.get()

            if account_number in accounts:
                accounts[account_number]["password"] = hash_password(new_password)

                # Update accounts.txt
                with open("accounts.txt", "w") as f:
                    for acc_num, details in accounts.items():
                        f.write(f"{acc_num},{details['name']},{details['password']},{details['balance']}\n")

                messagebox.showinfo("Success", "Password reset successful!")
                self.main_menu()
            else:
                messagebox.showerror("Error", "Account number not found.")

        tk.Button(self.root, text="Reset Password", command=reset_password).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=10)

    def account_menu(self, account_number):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Account Menu", font=("Arial", 16)).pack(pady=20)
        
        tk.Button(self.root, text="Check Balance", command=lambda: self.check_balance(account_number), width=20).pack(pady=10)
        tk.Button(self.root, text="Deposit", command=lambda: self.transaction_screen(account_number, "Deposit"), width=20).pack(pady=10)
        tk.Button(self.root, text="Withdrawal", command=lambda: self.transaction_screen(account_number, "Withdrawal"), width=20).pack(pady=10)
        tk.Button(self.root, text="Transaction History", command=lambda: self.transaction_history_screen(account_number), width=20).pack(pady=10)
        tk.Button(self.root, text="Logout", command=self.main_menu, width=20).pack(pady=10)

    def check_balance(self, account_number):
        accounts = load_accounts()
        balance = accounts[account_number]["balance"]
        messagebox.showinfo("Balance", f"Your current balance is: {balance}")

    def transaction_screen(self, account_number, transaction_type):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"{transaction_type}", font=("Arial", 16)).pack(pady=20)

        tk.Label(self.root, text="Amount:").pack()
        amount_entry = tk.Entry(self.root)
        amount_entry.pack()

        def perform_transaction():
            try:
                amount = float(amount_entry.get())
                accounts = load_accounts()

                if transaction_type == "Deposit":
                    accounts[account_number]["balance"] += amount
                    log_transaction(account_number, transaction_type, amount, "Success", accounts[account_number]["balance"])
                    messagebox.showinfo("Success", f"Deposit successful! Current balance: {accounts[account_number]['balance']}")
                elif transaction_type == "Withdrawal":
                    if accounts[account_number]["balance"] >= amount:
                        accounts[account_number]["balance"] -= amount
                        log_transaction(account_number, transaction_type, amount, "Success", accounts[account_number]["balance"])
                        messagebox.showinfo("Success", f"Withdrawal successful! Current balance: {accounts[account_number]['balance']}")
                    else:
                        log_transaction(account_number, transaction_type, amount, "Failed", accounts[account_number]["balance"])
                        messagebox.showerror("Error", "Insufficient balance.")

                # Update accounts.txt
                with open("accounts.txt", "w") as f:
                    for acc_num, details in accounts.items():
                        f.write(f"{acc_num},{details['name']},{details['password']},{details['balance']}\n")

                self.account_menu(account_number)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid amount.")

        tk.Button(self.root, text="Submit", command=perform_transaction).pack(pady=10)
        tk.Button(self.root, text="Back", command=lambda: self.account_menu(account_number)).pack(pady=10)

    def transaction_history_screen(self, account_number):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Transaction History", font=("Arial", 16)).pack(pady=20)

        transactions = load_transactions(account_number)

        if transactions:
            for transaction_type, amount, status, balance, date in transactions:
                tk.Label(self.root, text=f"{transaction_type} - {amount} - {status} - Balance: {balance} on {date}").pack()
        else:
            tk.Label(self.root, text="No transactions found.").pack()

        tk.Button(self.root, text="Back", command=lambda: self.account_menu(account_number)).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = BankingSystemApp(root)
    root.mainloop()
