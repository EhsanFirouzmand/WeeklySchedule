import sqlite3

# Connect to the database
conn = sqlite3.connect('schedule.db')

# Create a table to store the schedules
conn.execute('''CREATE TABLE IF NOT EXISTS schedules
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             day TEXT NOT NULL,
             task TEXT NOT NULL);''')

# Function to view the schedules
def view_schedules():
    cursor = conn.execute("SELECT * FROM schedules ORDER BY id;")
    for row in cursor:
        print("ID = ", row[0])
        print("Day = ", row[1])
        print("Task = ", row[2], "\n")

# Function to add a new schedule
def add_schedule(day, task):
    conn.execute("INSERT INTO schedules (day, task) VALUES (?, ?)", (day, task))
    conn.commit()
    print("Schedule added successfully!")

# Main function
def main():
    while True:
        print("1. View schedules")
        print("2. Add a new schedule")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            view_schedules()
        elif choice == 2:
            day = input("Enter the day (e.g. Monday, Tuesday, etc.): ")
            task = input("Enter the task: ")
            add_schedule(day, task)
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please enter a valid choice.")

# Call the main function
if __name__ == '__main__':
    main()

# Close the connection
conn.close()
