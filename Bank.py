def show_balance(balance):
    print("****************************")
    print(f"Your balance is Rs.{balance:.2f}")
    print("****************************")

def deposit(balance):
    amount = float(input("Enter an amount to be deposited:"))
    if amount<0:
        print("****************************")
        print("That's not a valid amount")
        print("****************************")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn:"))

    if amount > balance:
        print("****************************")
        print("Insufficient funds")
        print("****************************")
        return 0
    elif amount < 0:
        print("****************************")
        print("Amount must be grater than 0")
        print("****************************")
        return 0
    else:
        return amount

def main():
    balance=0
    is_running = True
    while is_running:
        print("****************************")
        print("Banking program")
        print("****************************")
        print("1.Show Balance \n2.Deposit \n3.Withdraw \n4.Exit")
        print("****************************")
        choice = input("Enter your choice(1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit(balance)
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("****************************")
            print("That is not a valid choice")
            print("****************************")
    print("****************************")
    print("Thank You have a nice day!")
    print("****************************")


if __name__ == '__main__':
    main()