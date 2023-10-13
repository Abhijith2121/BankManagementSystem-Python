import csv

counter = 1001
accounts = []


class Transaction:
    def __init__(self, account_name, amount, transaction_type):
        self.name = account_name
        self.amount = amount
        self.transaction_type = transaction_type

    def __str__(self):
        return f"Name: {self.name}, Amount: {self.amount}, Transaction Type: {self.transaction_type}"


class Account:
    def __init__(self, account_name, account_balance=0):
        global counter
        global accounts
        self.account_number = counter
        self.account_name = account_name
        self.account_balance = account_balance
        self.transactions = []
        counter += 1

    def deposit(self, amount):
        self.account_balance += amount
        tarnsaction = Transaction(self.account_name, amount, "Deposit")
        self.transactions.append(tarnsaction)
        print(f"Deposit of {amount} in {self.account_name} was successful")

    def withdraw(self, amount):
        if self.account_balance < amount:
            print("Withdrawal failed: Account balance insufficient")
        else:
            self.account_balance -= amount
            transaction = Transaction(self.account_name, amount, "Withdraw")
            self.transactions.append(transaction)
            print(f"Withdrawal of {amount} from {self.account_name} was successful")

    def check_balance(self):
        print("\nYour Account Balance is", self.account_balance)

    def transaction_history(self):
        if not self.transactions:
            print("No Transactions are done yet for this Account", self.account_number)
        else:
            for transaction in self.transactions:
                print(f"Transaction History of {self.account_name}")
                print(transaction)

    def save_transaction(self, filename):
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            field = ["Name", "Amount", "Transaction Type"]
            if file.tell() == 0:
                writer.writerow([field])
            for transaction in self.transactions:
                writer.writerow([transaction.name, transaction.amount, transaction.transaction_type])

    def close_account(self):
        account_index = accounts.index(self)
        if account_index is not None:
            del accounts[account_index]
            print(f"Account {self.account_name} with Account Number: {self.account_number} has been closed.")
        else:
            print(f"Account {self.account_name} not found.")


def find_account(accounts, account_number):
    for account in accounts:
        if account.account_number == account_number:
            return account
    return None


def login():
    while True:
        account_number = int(input("\nEnter your Account Number: "))
        account = find_account(accounts, account_number)
        if account is None:
            print("Account not found.")
        else:
            return account


while True:
    print("\n1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        account_name = input("\nEnter your Name: ")
        account = Account(account_name)
        accounts.append(account)
        print("\nAccount is created with Number", account.account_number)

    elif choice == 2:
        account = login()
        if account is not None:
            while True:
                print("\n1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. View Transaction History")
                print("5. Save Transaction History")
                print("6. Logout")
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    amount = float(input("Enter the Amount to deposit: "))
                    if amount <= 0:
                        print("Please enter an amount more than 0")
                    else:
                        account.deposit(amount)

                elif choice == 2:
                    amount = float(input("Enter the Amount to withdraw: "))
                    if amount <= 0:
                        print("Please enter an amount more than 0")
                    else:
                        account.withdraw(amount)

                elif choice == 3:
                    account.check_balance()

                elif choice == 4:
                    account.transaction_history()

                elif choice == 5:
                    account.transaction_history()
                    account.save_transaction(f"{account.account_name}.csv")

                elif choice == 6:
                    break

                else:
                    print("Wrong Choice")

    elif choice == 3:
        print("Thank you")
        break

    else:
        print("Wrong Choice")
