import mysql.connector

try:
    # 1. ESTABLISH THE CONNECTION
    # Replace 'your_password' with the one you use for Workbench!
    connection = mysql.connector.connect(
        host="localhost",       # The server location (your computer)
        user="root",            # Your username (usually 'root')
        password="csds@123", 
        database="assignment"  # The specific database you want to use
    )

    if connection.is_connected():
        print("Successfully connected to the database!")

        # 2. CREATE A CURSOR
        # The cursor is like your mouse—it executes the commands.
        cursor = connection.cursor()

        # 3. EXECUTE A QUERY
        query = "SELECT * FROM student"
        cursor.execute(query)

        # 4. FETCH THE RESULTS
        # .fetchall() grabs all rows the query found
        rows = cursor.fetchall()

        print("\n--- Student List ---")
        for row in rows:
            print(row)

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    # 5. CLOSE THE CONNECTION
    # Always close the door when you leave!
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("\nConnection closed.")