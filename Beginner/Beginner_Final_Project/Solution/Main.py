from Beginner.Beginner_Final_Project.Solution.BankAccount import BankAccount

def main():
    print("Welcome to the Simple Bank System")
    account_holder = input("Please enter the account holder's name: ")
    account = BankAccount(account_holder)

    while True:
        print("\nMenu:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Please choose an option: ")

        try:
            if choice == '1':
                amount = float(input("Enter amount to deposit: "))
                print(account.deposit(amount))
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                print(account.withdraw(amount))
            elif choice == '3':
                print(account.get_balance())
            elif choice == '4':
                print("Thank you for using Simple Bank System. Goodbye!")
                break
            else:
                print("Invalid option. Please select a valid menu option.")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()


