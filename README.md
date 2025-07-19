# account-managment-system1

---

## 🚀 Features

- 🔐 **Login System** using 4-digit PIN (3 attempts max)
- 💰 **Deposit** functionality with validation
- 💸 **Withdraw** with balance check
- 📊 **Balance Inquiry** feature
- 💾 Balance is stored in `balance.json` file
- ❌ Freezes account after 3 incorrect PIN attempts

---

## ✅ How to Run

1. Ensure you have Python 3 installed.
2. Create a `balance.json` file with initial balance:
```json
{
  "balance": 1000
}
python main.py

🔐 Default PIN
The default PIN for login is: 1234

You have 3 attempts. If all are wrong, the account will be frozen.

***Welcome to ABC Bank***
Enter your 4 digit pin: 1234
Login successful
Select Your Choice
1.Withdraw
2.Deposit
3.Check Balance
Enter the choice (1/2/3): 2
Enter the amount you want to Deposit: 500
Deposited Successfully ✅
Your account balance: 1500rs
Thanks for visiting
