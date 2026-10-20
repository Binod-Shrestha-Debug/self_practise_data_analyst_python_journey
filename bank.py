
balance = 5000
account_holder = "Binod Shrestha"
transactions = []

while True:
    print("\n===== PYTHON BANK MANAGEMENT SYSTEM =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Show Account Holder")
    print("5. Transaction History")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Current Balance: Rs.", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: Rs. "))

        if amount > 0:
            balance += amount
            transactions.append(f"Deposited: Rs. {amount:.2f}")
            print("Deposit successful!")
            print("New Balance: Rs.", balance)
        else:
            print("Please enter an amount greater than zero.")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: Rs. "))

        if amount <= 0:
            print("Please enter an amount greater than zero.")
        elif amount <= balance:
            balance -= amount
            transactions.append(f"Withdrawn: Rs. {amount:.2f}")
            print("Withdrawal successful!")
            print("Remaining Balance: Rs.", balance)
        else:
            print("Insufficient balance!")

    elif choice == "4":
        print("Account Holder:", account_holder)

    elif choice == "5":
        print("\n===== TRANSACTION HISTORY =====")

        if len(transactions) == 0:
            print("No transactions yet.")
        else:
            for transaction in transactions:
                print(transaction)

    elif choice == "6":
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid choice. Please try again.")
