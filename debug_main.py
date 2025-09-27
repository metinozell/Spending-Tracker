import json, os, datetime
def load_expenses():
    if os.path.exists("expenses.json"):
        with open("expenses.json","r",encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []
def save_expenses(expenses):
    with open("expenses.json","w",encoding="utf-8") as file:
        json.dump(expenses,file,indent=4,ensure_ascii=False)

def display_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.\n")
    else:
        print("\nAll Recorded Expenses:")
        for idx,exp in enumerate(expenses,1):
            print(f"{idx}. Date: {exp['date']}, Category: {exp['category']}, Amount: {exp['amount']}, Description: {exp['description']}")
        print()

def calculate_total_and_by_category(expenses):
    total=sum(exp['amount'] for exp in expenses)
    print(f"\nTotal Spending: ${total:.2f}")
    category_totals={}
    for exp in expenses:
        category=exp['category']
        if category in category_totals:
            category_totals[category]+=exp['amount']
        else:
            category_totals[category]=exp['amount']
    print("\nSpending by Category:")
    for category,amount in category_totals.items():
        print(f"{category}: ${amount:.2f}")
    print()

def filtered_expenses_by_date(expenses,start_date,end_date):         
    filtered_expenses=[exp for exp in expenses if start_date<=exp['date']<=end_date]
    total=sum(exp['amount'] for exp in filtered_expenses)
    print(f"\nTotal spending from {start_date} to {end_date}: ${total:.2f}")

    category_totals={}
    for exp in filtered_expenses:
        category=exp['category']
        category_totals[category]+=exp['amount']

    print("\nSpending by Category:")
    for category,amount in category_totals.items():
        print(f"{category}: ${amount:.2f}")
    print()

    print(f"Expenses from {start_date} to {end_date}:")
    for idx,exp in enumerate(filtered,1):
        print(f"{idx}. Date: {exp['date']}, Category: {exp['category']}, Amount: {exp['amount']}, Description: {exp['description']}")
    print()
    return filtered_expenses

print("Welcome to the Spending Tracker App!")
while True:
    print("Please choose an option:\n")
    print("1. Add a new expense.")
    print("2. View all expenses.")
    print("3. Total spending calculation.")
    print("4. Filter expenses by date range.")
    print("5. Exit.")
    try:
        choice=int(input("Enter your choice (1-5): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.\n")
        continue
    
    if choice==1:
        while True:
            date=input("Enter the date (YYYY-MM-DD): ")
            try:
                datetime.datetime.strptime(date,"%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.\n")

        category=input("Enter the category (e.g., Food, Transport): ")
        
        while True:
            try:
                amount=float(input("Enter the amount: "))
                if amount<=0:
                    print("Amount must be a positive number. Please try again.\n")
                    continue
                break
            except ValueError:  
                print("Invalid amount. Please enter a numeric value.\n")

        description=input("Enter a description (optional): ") or "No description"

        expense={
            "date": date,
            "category":category,
            "amount":amount,
            "description":description
            }
        expenses=load_expenses()
        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!\n")

    elif choice==2:
        expenses=load_expenses()
        display_expenses(expenses)

    elif choice==3:
        expenses=load_expenses()
        calculate_total_and_by_category(expenses)

    elif choice==4:
        expenses=load_expenses()
        start_date=input("Enter the start date (YYYY-MM-DD): ")
        end_date=input("Enter the end date (YYYY-MM-DD): ") 
        filtered=filtered_expenses_by_date(expenses,start_date,end_date)


    elif choice==5:
        print("Thank you for using the Spending Tracker App!")
        break