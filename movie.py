import mysql.connector

def movie_booking():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="csds@123",  # Use your password
            database="movie_db"
        )
        cursor = db.cursor(dictionary=True, buffered=True)

        while True:
            print("\n--- MOVIE TICKET BOOKING SYSTEM ---")
            print("1. View Movies")
            print("2. Book a Ticket")
            print("3. Exit")
            choice = input("Select an option: ")

            if choice == '1':
                cursor.execute("SELECT * FROM movies")
                for movie in cursor.fetchall():
                    print(f"[{movie['movie_id']}] {movie['title']} - ₹{movie['price']} (Seats Left: {movie['total_seats']})")

            elif choice == '2':
                name = input("Enter your name: ")
                m_id = int(input("Enter Movie ID: "))
                count = int(input("How many seats? "))

                # Check if seats are available
                cursor.execute("SELECT title, price, total_seats FROM movies WHERE movie_id = %s", (m_id,))
                movie = cursor.fetchone()

                if movie and movie['total_seats'] >= count:
                    cost = movie['price'] * count
                    
                    # 1. Deduct seats from Movie table
                    new_seats = movie['total_seats'] - count
                    cursor.execute("UPDATE movies SET total_seats = %s WHERE movie_id = %s", (new_seats, m_id))
                    
                    # 2. Add record to Bookings table
                    cursor.execute("INSERT INTO bookings (customer_name, movie_id, seats_booked, total_cost) VALUES (%s, %s, %s, %s)",
                                   (name, m_id, count, cost))
                    
                    db.commit() # Save changes to both tables
                    print(f"Success! Total Cost: ₹{cost}. Enjoy {movie['title']}!")
                else:
                    print("Error: Not enough seats or invalid Movie ID.")

            elif choice == '3':
                break

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    finally:
        db.close()

movie_booking()