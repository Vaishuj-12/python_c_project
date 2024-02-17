
import sqlite3

def create_expense_table():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expenses
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  date TEXT, 
                  amount REAL, 
                  category TEXT, 
                  description TEXT)''')
    conn.commit()
    conn.close()

def add_expense(date, amount, category, description):
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('''INSERT INTO expenses (date, amount, category, description) 
                 VALUES (?, ?, ?, ?)''', (date, amount, category, description))
    conn.commit()
    conn.close()

def view_expenses():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM expenses''')
    expenses = c.fetchall()
    conn.close()
    return expenses

def main():
    create_expense_table()
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            add_expense(date, amount, category, description)
            print("Expense added.")
        elif choice == "2":
            expenses = view_expenses()
            if expenses:
                print("Expenses:")
                for expense in expenses:
                    print(expense)
            else:
                print("No expenses.")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

