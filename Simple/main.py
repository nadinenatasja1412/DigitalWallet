class Ewallet:

    def __init__(self, owner):
        
        self.owner = owner
        self.balance = 0.0
        
    def check(self):
        print(f"\n{self.owner}'s Wallet Balace: ${self.balance: .2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} deposit successfully Added")
        else:
            print("Invalid deposit")
    
    def withdraw(self, amount):
        if amount <= 0 :
            print("Invalid withdrawal amount.")
        
        elif amount > self.balance:
            print ("Insufficient balance")
        
        else:
            self.balance -= amount
            print(f"\n${amount:.2f} withdrawn successfully")
        
def main():
    print("💰WELCOME TO E-WALLET APPS 💳 ")
    name = input("enter y/n to create a wallet: ")
    wallet = Ewallet (name)

    while True:
        print("\n 🎉 Menu: ")

        print ("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Input choice {1 - 4}: ")

        if choice == '1':
            wallet.check()
        elif choice == '2':
            try:
                amount = float(input("Enter the amount of deposit: "))

                wallet.deposit(amount)
            except ValueError:
                print ("Please enter a valid number")
        elif choice == '3':
            try:
                withdraw = float(input("Enter the amount of withdraw: "))

                wallet.withdraw(withdraw)
            except ValueError:
                print ("Please enter a valid number")
            
        elif choice == '4':
            print(f"Goodbye bitch! {wallet.owner}")
            break
        
        else :
            print("Incorrect Choices\n")

if __name__ == "__main__":
    main()