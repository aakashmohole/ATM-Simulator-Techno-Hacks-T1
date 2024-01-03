#[ATM Simulator -by Aakash Mohole]
def check_balance(balance):
    print("Choose account type:\n1. Saving\n2. Current")
    acc_type = int(input("Enter here (1-2): "))
    if acc_type == 1:
        account_number = int(input("Enter Account Number: "))
        pin = input("Enter 6 Digit PIN: ")
        print("\n---------------------------------------------")
        print(f"Your Current Available Balance is: {balance} Rs")
        print("-----------------------------------------------")
    elif acc_type == 2:
        account_number = input("Enter Account Number:  ")
        phone_no = input("Enter phone no: ")
        otp = input("Enter OTP: ")
        print("\n---------------------------------------------")
        print(f"Your Current Available Balance is: {balance} Rs")
        print("-----------------------------------------------")
    else:
        print("Invalid credentials. Please try again.")


def deposit_amount(balance):
    print("Choose account type:\n1. Saving\n2. Current")
    acc_type = int(input("Enter here (1-2): "))
    if acc_type == 1:
        account_number = int(input("Enter Account Number:  "))
        pin = input("Enter 6 digit pin: ")
        dep_amount = int(input("Enter amount to deposit: "))
        new_balance = balance + dep_amount
        print("\n---------------------------------------------")
        print(f"Your amount {dep_amount} is deposited! Your new balance is {new_balance} Rs")
        print("-----------------------------------------------")
        return new_balance

    elif acc_type == 2:
        account_number = input("Enter Account Number:  ")
        phone_no = input("Enter phone no: ")
        otp = input("Enter 6 Digit PIN: ")
        dep_amount = int(input("Enter amount to deposit: "))
        new_balance = balance + dep_amount
        print("\n---------------------------------------------")
        print(f"Your amount {dep_amount} is deposited! Your new balance is {new_balance} Rs")
        print("-----------------------------------------------")
        return new_balance

    else:
        print("Invalid credentials. Please try again.")
        return balance


def withdraw_amount(balance):
    print("Choose account type:\n1. Saving\n2. Current")
    acc_type = int(input("Enter here (1-2): "))
    if acc_type == 1:
        account_number = int(input("Enter Account Number:  "))
        pin = input("Enter 6 digit pin: ")
        wit_amount = int(input("Enter amount to withdraw: "))
        new_balance = balance - wit_amount
        print("\n---------------------------------------------")
        print(f"Your amount {wit_amount} is withdrawn! Your new balance is {new_balance} Rs")
        print("-----------------------------------------------")
        return new_balance

    elif acc_type == 2:
        account_number = input("Enter Account Number:  ")
        phone_no = input("Enter phone no: ")
        otp = input("Enter 6 Digit PIN: ")
        dep_amount = int(input("Enter amount to deposit: "))
        wit_amount = int(input("Enter amount to withdraw: "))
        new_balance = balance - wit_amount
        print("\n---------------------------------------------")
        print(f"Your amount {wit_amount} is withdrawn! Your new balance is {new_balance} Rs")
        print("-----------------------------------------------")
        return new_balance

    else:
        print("Invalid credentials. Please try again.")
        return balance


def main():
    # account_number = 0
    # pin = 0
    # phone_no = 0
    # otp = 0

    balance = 10000

    while True:
        print("\n*** WELCOME TO MYBANK ****\n")
        print("1. Check Bank Balance\n2. Deposit Amount\n3. Withdraw Amount\n4. Exit")

        choice = int(input("Enter here (1-4): "))
        print('\n')

        if choice == 1:
            check_balance(balance)
        elif choice == 2:
            balance = deposit_amount(balance)
        elif choice == 3:
            balance = withdraw_amount(balance)
        elif choice == 4:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()

