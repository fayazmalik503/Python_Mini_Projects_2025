# Mini ATM Simulator (Text-based)

# 🎯 Features:
# User se:

# 💰 Balance check karna

# ➕ Amount deposit karna

# ➖ Amount withdraw karna

# ❌ Exit karna


balance = 1000 # starting balance

while True:
    print("\n===== Welcome to Mini ATM =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter you choice (1-4): ")

    if choice =="1":
        print(f"💰 Your current balance is: {balance}")
    
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"✅ {amount} deposited successfully!")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"💸 {amount} withdrawn successfully!")
        
    
    elif choice == "4":
            print("👋 Thank you for using Mini ATM. Goodbye!")
            break
    
    
    else:
        print("❌ Invalid choice! Please select 1 to 4.")