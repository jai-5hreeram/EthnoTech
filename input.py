import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="csds@123", 
        database="assignment"
    )
    # Use buffered=True globally to avoid the "Unread Results" error
    mycursor = mydb.cursor(buffered=True)

    choice = input("Do you want to (A)dd, (D)elete,(U)pdate or (V)iew? ").upper()

    query = ""
    
    match choice:
        case 'A':
            query = "INSERT INTO dept (id, name) VALUES ('13', 'MPhil')"
        case 'D':
            query = "DELETE FROM student WHERE id=12"
        case 'U':
            query= "UPDATE `assignment`.`dept` SET `name` = NULL WHERE (`id` = '12');"
        case 'V':
            query = "SELECT * FROM student"
        case _:
            print("Invalid choice!")

    if query:
        # 1. Execute the query decided in match-case
        mycursor.execute(query)

        # 2. Handle the results based on the choice
        if choice == 'V':
            rows = mycursor.fetchall()
            if not rows:
                print("The table is empty.")
            else:
                print("\n--- Student List ---")
                for row in rows:
                    print(row)
        else:
            mydb.commit()
            print(f"Action successful. {mycursor.rowcount} row(s) affected.")

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if 'mydb' in locals() and mydb.is_connected():
        mycursor.close()
        mydb.close()
