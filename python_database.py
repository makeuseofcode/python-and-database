import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
               first_name TEXT,
               last_name TEXT,
               email TEXT UNIQUE,
               password TEXT
               )
""")
conn.commit()

def register_user():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    
    while True:
        email = input("Enter your email: ")
        password1 = input("Enter your password: ")
        password2 = input("Confirm your password: ")

        # Check password correctness
        if password1 == password2:
            try:
                cursor.execute("""
                    INSERT INTO users (first_name, last_name, email, password)
                    VALUES (?, ?, ?, ?)
                """, (first_name, last_name, email, password2))
                conn.commit()
                print("You have successfully created an account.")
                break
            except sqlite3.IntegrityError:
                print("Error: This email is already registered.")
        else:
            print("Your passwords must match.")

register_user()
cursor.close()

conn.close()