# Banking System

## Description
The **Banking System** is a console and GUI-based application designed to enable users to create accounts, perform secure banking transactions, and manage their finances effectively. This project ensures data security through password hashing and employs file handling for persistent storage of user accounts and transactions.

## Features
- **Account Management**: Create new accounts and securely store account details.
- **User Authentication**: Secure login functionality with hashed password storage.
- **Banking Transactions**:
  - Deposit and withdraw money.
  - Check account balance.
- **Transaction History**: View detailed records of all transactions.
- **Forgot Password**: Reset password functionality.

## File Handling
### Accounts File (`accounts.txt`):
- Stores user details in the following format:

  ```
  Account Number, Name, Password (Hashed), Balance
  ```
  **Example:**
  ```
  000001,Dheeraj,ca719b5682c1d495109493f429bc313ed3e3a1c3852a967b7c164f45291ae7b6,151200.0
  ```

### Transactions File (`transactions.txt`):
- Stores transaction details in the following format:

  ```
  Account Number, Transaction Type (Deposit/Withdrawal), Amount, Status, Balance, Date
  ```
  **Example:**
  ```
  000001,Withdrawal,100.0,Success,99900.0,2025-01-03
  ```

## Application Flow
### Main Menu
```plaintext
Welcome to the Banking System!
1. Create Account
2. Login
3. Forgot Password
4. Exit
```

### Create Account
- Inputs: Name, Initial Deposit, Password.
- Generates a unique account number and saves account details to `accounts.txt`.
- Example Output:
  ```plaintext
  Enter your name: John Doe
  Enter your initial deposit: 1000
  Your account number: 123456 (Save this for login)
  Account created successfully!
  ```

### Login
- Inputs: Account Number, Password.
- Validates credentials against stored details in `accounts.txt`.
- Redirects to the **Account Menu** upon successful login.

### Account Menu
- Options:
  - Check Balance
  - Deposit
  - Withdrawal
  - Transaction History
  - Logout

### Transactions
- **Deposit**: Adds the specified amount to the user’s balance and logs the transaction in `transactions.txt`.
- **Withdrawal**: Deducts the specified amount if sufficient balance exists and logs the transaction.
- Displays error for insufficient balance.

### Transaction History
- Displays a list of all transactions for the logged-in account with details such as type, amount, status, balance, and date.

### Forgot Password
- Allows users to reset their password by entering their account number and a new password.
- Updates the account details in `accounts.txt`.

## Implementation Details
### Technology Stack
- **Programming Language**: Python
- **Libraries**: Tkinter (for GUI), hashlib (for password hashing), os (for file handling), datetime (for timestamping).

### Security Features
- Passwords are hashed using SHA-256 before being stored.
- User data and transaction logs are securely handled through file operations.

### Error Handling
- Input validation for numeric fields (e.g., deposit/withdrawal amounts).
- Comprehensive error messages for incorrect credentials, insufficient balance, and invalid inputs.

## Getting Started
### Prerequisites
- Python 3.x installed on your system.

### Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd banking-system
   ```
3. Run the application:
   ```bash
   python banking_system.py
   ```

## Usage
1. Launch the application.
2. Create an account or log in using existing credentials.
3. Perform desired transactions or manage your account as needed.

## Future Enhancements
- Implement database storage for scalability.
- Add support for online money transfers between accounts.
- Integrate data encryption for enhanced security.

## License
This project is licensed under the [MIT License](LICENSE).

---
Developed with 💻 and ☕ by Dheeraj Kumar
