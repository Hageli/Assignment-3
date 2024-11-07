import psycopg2


def menu():
    print("\n1. Change database")
    print("2. Read data")
    print("0. Exit")
    choice = int(input("Enter choice: "))
    return choice

def change_database():
    print("\nWhere would you like to read data from?")
    print("1. Finland")
    print("2. Sweden")
    print("3. Norway")
    print("4. Estonia")
    choice = int(input("Enter choice: "))
    return choice

def setup_connections():
    # FINLAND
    finland_db_conn = psycopg2.connect(host="localhost", database="a3_finland", user="postgres", password="admin")

    # SWEDEN
    sweden_db_conn = psycopg2.connect(host="localhost", database="a3_sweden", user="postgres", password="admin")

    # NORWAY
    norway_db_conn = psycopg2.connect(host="localhost", database="a3_norway", user="postgres", password="admin")

    # ESTONIA
    estonia_db_conn = psycopg2.connect(host="localhost", database="a3_estonia", user="postgres", password="admin")

    return finland_db_conn, sweden_db_conn, norway_db_conn, estonia_db_conn

def main():
    finland_db_conn, sweden_db_conn, norway_db_conn, estonia_db_conn = setup_connections()

    # SETUP DATABASE CURSORS
    finland_cur = finland_db_conn.cursor()
    sweden_cur = sweden_db_conn.cursor()
    norway_cur = norway_db_conn.cursor()
    estonia_cur = estonia_db_conn.cursor()

    # CURRENT CURSOR
    current_cur = None

    print("Welcome to the database!")
    country = change_database()
    
    # SET THE CURRENT CURSOR TO THE SELECTED COUNTRY, DEFAULT IS FINLAND
    match country:
        case 1:
            current_cur = finland_cur
        case 2:
            current_cur = sweden_cur
        case 3:
            current_cur = norway_cur
        case 4:
            current_cur = estonia_cur
        case _:
            print("Invalid choice, defaulting to Finland")
            current_cur = finland_cur

    while(True):
        choice = menu()
        match choice:
            # CHANGE DATABASE
            case 1:
                country = change_database()
                match country:
                    case 1:
                        current_cur = finland_cur
                    case 2:
                        current_cur = sweden_cur
                    case 3:
                        current_cur = norway_cur
                    case 4:
                        current_cur = estonia_cur
                    case _:
                        print("Invalid choice, defaulting to Finland\n")
                        current_cur = finland_cur
            
            # READ DATA
            case 2:
                print("\nWhat table would you like to read from?")
                print("1. customer")
                print("2. item")
                print("3. orders")
                print("4. storage_info")
                table = input("Enter choice: ")

                # SET THE TABLE TO READ 
                match table:
                    case "1":
                        table = "customer"
                    case "2":
                        table = "item"
                    case "3":
                        table = "orders"
                    case "4":
                        table = "storage_info"
                    case _:
                        print("Invalid choice, defaulting to customer")
                        table = "customer"

                # EXECUTING THE DATABASE QUERY
                print()
                current_cur.execute(f"SELECT * FROM {table}")
                rows = current_cur.fetchall()
                for row in rows:
                    print(row)
            
            # EXIT SYSTEM
            case 0:
                break

            # INVALID CHOICE, DEFAULT CASE
            case _:
                print("Invalid choice, please try again")

    # CLOSING THE DATABASE CONNECTIONS
    finland_cur.close()
    sweden_cur.close()
    norway_cur.close()
    estonia_cur.close()
    finland_db_conn.close()
    sweden_db_conn.close()
    norway_db_conn.close()
    estonia_db_conn.close() 
    print("Exiting database system...")

if __name__ == "__main__":
    main()