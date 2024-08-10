import datetime

class ATMSimulation:
    def __init__(self, pin, initial_balance=0.0):
        self.pin = pin
        self.balance = initial_balance
        self.transactions = []

    def balance_inquiry(self):
        print(f"Your balance is: Rs{self.balance:.2f}")

    def cash_withdrawal(self):
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Amount must be greater than 0.")
            elif amount > self.balance:
                print("Insufficient funds.")
            else:
                self.balance -= amount
                transaction = f"{datetime.datetime.now()} - Withdrawal: -Rs{amount:.2f}"
                self.transactions.append(transaction)
                print(f"Withdrew Rs{amount:.2f}. New balance: Rs{self.balance:.2f}")
        except ValueError:
            print("Invalid input. Please enter a numeric amount.")

    def cash_deposit(self):
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                self.balance += amount
                transaction = f"{datetime.datetime.now()} - Deposit: +Rs{amount:.2f}"
                self.transactions.append(transaction)
                print(f"Deposited Rs{amount:.2f}. New balance: Rs{self.balance:.2f}")
        except ValueError:
            print("Invalid input. Please enter a numeric amount.")

    def change_pin(self):
        current_pin = input("Enter current PIN: ")
        if current_pin == self.pin:
            new_pin = input("Enter new PIN: ")
            confirm_pin = input("Confirm new PIN: ")
            if new_pin == confirm_pin:
                self.pin = new_pin
                print("PIN successfully changed.")
            else:
                print("PINs do not match. Please try again.")
        else:
            print("Incorrect current PIN.")

    def view_transactions(self):
        if not self.transactions:
            print("No transactions yet.")
        else:
            print("Transaction History:")
            for transaction in self.transactions:
                print(transaction)

def main():
    pin = input("Enter your PIN: ")
    atm = ATMSimulation(pin)

    while True:
        print("\nATM Menu:")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Change PIN")
        print("5. View Transactions")
        print("6. Exit")

        choice = input("Select an option (1-6): ")

        if choice == "1":
            atm.balance_inquiry()
        elif choice == "2":
            atm.cash_withdrawal()
        elif choice == "3":
            atm.cash_deposit()
        elif choice == "4":
            atm.change_pin()
        elif choice == "5":
            atm.view_transactions()
        elif choice == "6":
            print("Exiting... Thank you for using the ATM!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
