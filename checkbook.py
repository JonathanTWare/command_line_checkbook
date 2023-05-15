import os


filename = "balance.txt"
balance = 5000.00


if os.path.exists(filename):
    
    try:
        with open(filename, "r") as f:
            balance = float(f.read().strip())
    except ValueError:
        print("Error: invalid balance value in file")
    except:
        print("Error: failed to read balance file")



def view_balance():
    print(f"Hi there, your current balance is: ${balance:.2f}")

while True:
    print("\n---- Welcome To The Terminal ATM! ----\n")
    print("What would you like to do today?\n")
    print("1) View Current Balance")
    print("2) Make a Withdraw")
    print("3) Make a Deposit")
    print("4) Exit\n")

    user_pick = input("What would you like to do today? ")
    
    if user_pick == "1":
        view_balance()
    elif user_pick == "2":
        amount = float(input("\nEnter an amount to withdraw: "))
        if balance - amount < 0:
            print("\nSorry, insufficient funds.")
        else:
            balance -= amount
            print(f"\nYou have made a successful withdraw of ${amount:.2f}. Your new balance is: ${balance:.2f}\n")
    elif user_pick == "3":
        amount = float(input("\nEnter amount to deposit: "))
        balance += amount
        print(f"\nYou have made a deposit of ${amount:.2f}. Your new balance is: ${balance:.2f}\n")
    elif user_pick == "4":
        with open(filename, "w") as f:
            f.write(str(balance))
        print("\nThank you for using Jon's Terminal ATM!")
        break
    else:
        print("\nYou have picked an invalid choice: ", user_pick)






 






