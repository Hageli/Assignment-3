import psycopg2

def dbInit():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="admin"
    )

    # AUTOMATICALLY COMMIT ALL THE CHANGES MADE
    conn.autocommit = True
    cur = conn.cursor()

    # CREATE THE DATABASES
    cur.execute("CREATE DATABASE a3_finland")
    cur.execute("CREATE DATABASE a3_sweden")
    cur.execute("CREATE DATABASE a3_norway")
    cur.execute("CREATE DATABASE a3_estonia")

    # CLOSE THE CONNECTION
    cur.close()
    conn.close()

    ### CREATE TABLES ###
    # CONNECT TO THE a3_finland DATABASE
    conn = psycopg2.connect(
        host="localhost",
        database="a3_finland",
        user="postgres",
        password="admin"
    )
    conn.autocommit = True
    cur = conn.cursor()

    # CREATE CUSTOMER
    cur.execute("""
        CREATE TABLE IF NOT EXISTS customer (
                id INT PRIMARY KEY,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                order_history INT ARRAY
                )""")
    
    # CREATE ITEM
    cur.execute("""
        CREATE TABLE IF NOT EXISTS item (
                id INT PRIMARY KEY,
                name VARCHAR(100),
                price DECIMAL(10, 2)
                )""")
    
    # CREATE ORDERS
    cur.execute("""
        CREATE TABLE IF NOT EXISTS orders (
                id INT PRIMARY KEY,
                customer_id INT,
                item_id INT ARRAY,
                price DECIMAL(10, 2)
                )""")
    
    # CREATE STORAGE_INFO
    cur.execute("""
        CREATE TABLE IF NOT EXISTS storage_info (
                item_id INT PRIMARY KEY,
                amount INT,
                location VARCHAR(50)
                )""")
    
    # INSERT CUSTOMER
    cur.execute("""
        INSERT INTO customer (id, first_name, last_name, order_history) VALUES 
            (1,	'William', 'Fagerholm', '{1}'),
            (2,	'Emma', 'Granlund', '{2,3}'),
            (3,	'Miro', 'Hagelberg', '{4,5}'),
            (4,	'Eero', 'Holopainen', '{}'),
            (5,	'Katja', 'Ijäs', '{}'),
            (6,	'Arttu', 'Isotamm', '{6}')
                """)
    
    # INSERT ITEM
    cur.execute("""
        INSERT INTO item (id, name, price) VALUES 
            (1, 'Mämmi', 4.40),
            (2,	'Meatball',	3.10),
            (3,	'Baseball bat', 76.20),
            (4,	'Reindeer milk', 7.00),
            (5,	'Audi R8', 65000.00),
            (6,	'Moomin mug', 12.90),
            (7,	'Smoked sausage', 2.70),
            (8,	'Ice skates', 49.99),
            (9,	'Car tires (used)', 200.00),
            (10, 'Carelian pie', 1.50)
                """)
    
    # INSERT ORDERS
    cur.execute("""
        INSERT INTO orders (id, customer_id, item_id, price) VALUES 
            (1,	1, '{3}', 76.20),
            (2,	2, '{1,2}', 7.50),
            (3,	2, '{8,10}', 51.49),
            (4,	3, '{6,7,9}', 215.60),
            (5,	3, '{4}', 7.00),
            (6,	6, '{5}', 65000.00)
                """)
    
    # INSERT STORAGE_INFO
    cur.execute("""
        INSERT INTO storage_info (item_id, amount, location) VALUES 
            (1, 11, 'Finland'),
            (2, 7, 'Sweden'),
            (3, 4, 'Finland'),
            (4, 60, 'Finland'),
            (5, 1, 'Finland'),
            (6, 68, 'Finland'),
            (7, 7, 'Finland'),
            (8, 32, 'Finland'),
            (9, 54, 'Finland'),
            (10, 200, 'Finland')
                """)
    
    cur.close()
    conn.close()

    # CONNECT TO THE a3_sweden DATABASE
    conn = psycopg2.connect(
        host="localhost",
        database="a3_sweden",
        user="postgres",
        password="admin"
    )
    conn.autocommit = True
    cur = conn.cursor()

    # CREATE CUSTOMER
    cur.execute("""
        CREATE TABLE IF NOT EXISTS customer (
                id INT PRIMARY KEY,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                order_history INT ARRAY
                )""")
    
    # CREATE ITEM
    cur.execute("""
        CREATE TABLE IF NOT EXISTS item (
                id INT PRIMARY KEY,
                name VARCHAR(100),
                price DECIMAL(10, 2)
                )""")
    
    # CREATE ORDERS
    cur.execute("""
        CREATE TABLE IF NOT EXISTS orders (
                id INT PRIMARY KEY,
                customer_id INT,
                item_id INT ARRAY,
                price DECIMAL(10, 2)
                )""")
    
    # CREATE STORAGE_INFO
    cur.execute("""
        CREATE TABLE IF NOT EXISTS storage_info (
                item_id INT PRIMARY KEY,
                amount INT,
                location VARCHAR(50)
                )""")
    
    # INSERT CUSTOMER
    cur.execute("""
        INSERT INTO customer (id, first_name, last_name, order_history) VALUES 
            (1, 'Mikko', 'Arvidsson', '{1,2}'),
            (2, 'Johan', 'Boren', '{}'),
            (3, 'Erik', 'Carlsson', '{3}'),
            (4, 'Emilia', 'Davidsson', '{4}'),
            (5, 'Johanna', 'Eklund', '{5}')
                """)
    
    # INSERT ITEM
    cur.execute("""
        INSERT INTO item (id, name, price) VALUES 
            (1,	'Meatball', 3.10),
            (2,	'Ikea table', 20.55),
            (3,	'Nobel price (used)', 100.99),
            (4,	'Golf club', 200.75),
            (5,	'T-shirt', 5.45)
                """)
    
    # INSERT ORDERS
    cur.execute("""
        INSERT INTO orders (id, customer_id, item_id, price) VALUES 
            (1,	1, '{1,5}', 8.55),
            (2,	1, '{3}', 100.99),
            (3,	3, '{2,4}', 221.30),
            (4,	4, '{1,3}', 104.09),
            (5,	5, '{2}', 20.55)
                """)
    
    # INSERT STORAGE_INFO
    cur.execute("""
        INSERT INTO storage_info (item_id, amount, location) VALUES 
            (1,	7, 'Sweden'),
            (2,	3, 'Sweden'),
            (3,	8, 'Sweden'),
            (4,	10, 'Sweden'),
            (5,	20, 'Sweden')
                """)
    
    cur.close()
    conn.close()

    # CONNECT TO THE a3_norway DATABASE
    conn = psycopg2.connect(
        host="localhost",
        database="a3_norway",
        user="postgres",
        password="admin"
    )

    conn.autocommit = True
    cur = conn.cursor()

    # CREATE CUSTOMER
    cur.execute("""
        CREATE TABLE IF NOT EXISTS customer (
                id INT PRIMARY KEY,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                order_history INT ARRAY
                )""")
    
    # CREATE ITEM
    cur.execute("""
        CREATE TABLE IF NOT EXISTS item (
                id INT PRIMARY KEY,
                name VARCHAR(100),
                price DECIMAL(10, 2)
                )""")
    
    # CREATE ORDERS
    cur.execute("""
        CREATE TABLE IF NOT EXISTS orders (
                id INT PRIMARY KEY,
                customer_id INT,
                item_id INT ARRAY,
                price DECIMAL(10, 2)
                )""")
    
    # CREATE STORAGE_INFO
    cur.execute("""
        CREATE TABLE IF NOT EXISTS storage_info (
                item_id INT PRIMARY KEY,
                amount INT,
                location VARCHAR(50)
                )""")
    
    # INSERT CUSTOMER
    cur.execute("""
        INSERT INTO customer (id, first_name, last_name, order_history) VALUES 
            (1,	'Olaf',	'Jörgensen', '{1,4}'),
            (2,	'Amelia', 'Kristiansen', '{2}'),
            (3,	'Justus', 'Laamanen', '{3}'),
            (4,	'Ari', 'Mägi', '{}'),
            (5,	'Richard', 'Nagelsmann', '{5}'),
            (6,	'Anna', 'Osman', '{6,7}')
                """)
    
    # INSERT ITEM
    cur.execute("""
        INSERT INTO item (id, name, price) VALUES 
            (1,	'Flag', 34.75),
            (2,	'Cooking oil', 5.60),
            (3,	'Hair spray', 2.99),
            (4,	'Snowmobile', 1200.00),
            (5,	'Salmon', 10.90),
            (6,	'Husky puppy', 300.99)
                """)
    
    # INSERT ORDERS
    cur.execute("""
        INSERT INTO orders (id, customer_id, item_id, price) VALUES 
            (1,	1, '{2}', 5.60),
            (2,	2, '{3,4}', 1202.99),
            (3,	3, '{5}', 10.90),
            (4,	1, '{6}', 300.99),
            (5,	5, '{1,4}', 1234.75),
            (6,	6, '{5,6}', 311.89),
            (7,	6, '{4,6}', 1500.99)
                """)
    
    # INSERT STORAGE_INFO
    cur.execute("""
        INSERT INTO storage_info (item_id, amount, location) VALUES 
            (1,	25, 'Norway'),
            (2,	500, 'Norway'),
            (3,	40, 'Norway'),
            (4,	5, 'Norway'),
            (5,	23, 'Norway'),
            (6,	3, 'Norway')
                """)
    
    cur.close()
    conn.close()

    # CONNECT TO THE a3_estonia DATABASE
    conn = psycopg2.connect(
        host="localhost",
        database="a3_estonia",
        user="postgres",
        password="admin"
    )

    conn.autocommit = True
    cur = conn.cursor()

    # CREATE CUSTOMER
    cur.execute("""
        CREATE TABLE IF NOT EXISTS customer (
                id INT PRIMARY KEY,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                order_history INT ARRAY
                )""")
    
    # CREATE ITEM
    cur.execute("""
        CREATE TABLE IF NOT EXISTS item (
                id INT PRIMARY KEY,
                name VARCHAR(100),
                price DECIMAL(10, 2)
                )""")
    
    # CREATE ORDERS
    cur.execute("""
        CREATE TABLE IF NOT EXISTS orders (
                id INT PRIMARY KEY,
                customer_id INT,
                item_id INT ARRAY,
                price DECIMAL(10, 2)
                )""")
    
    # CREATE STORAGE_INFO
    cur.execute("""
        CREATE TABLE IF NOT EXISTS storage_info (
                item_id INT PRIMARY KEY,
                amount INT,
                location VARCHAR(50)
                )""")
    
    # INSERT CUSTOMER
    cur.execute("""
        INSERT INTO customer (id, first_name, last_name, order_history) VALUES 
            (1,	'Elias', 'Pettersson', '{}'),
            (2,	'Pyry', 'Rainos', '{1}'),
            (3,	'Christopher', 'Sundin', '{2,3}'),
            (4,	'Oskari', 'Tuomala', '{4,5}'),
            (5,	'Alisa', 'Weckman', '{6}'),
            (6,	'Henrik', 'Zetterberg', '{7}'),
            (7,	'Otto',	'Äijälä', '{8}')
                """)
    
    # INSERT ITEM
    cur.execute("""
        INSERT INTO item (id, name, price) VALUES 
            (1,	'Mämmi', 4.40),
            (2,	'Meatball', 3.10),
            (3,	'Baseball bat', 76.20),
            (4,	'Reindeer milk', 7.00),
            (5,	'Audi R8', 65000.00),
            (6,	'Moomin mug', 12.90),
            (7,	'Smoked sausage', 2.70),
            (8,	'Ice skates', 49.99),
            (9,	'Car tires (used)', 200.00),
            (10, 'Carelian pie', 1.50)
                """)
    
    # INSERT ORDERS
    cur.execute("""
        INSERT INTO orders (id, customer_id, item_id, price) VALUES 
            (1,	2, '{1,2}', 7.50),
            (2,	3, '{3}', 76.20),
            (3,	3, '{8}', 49.99),
            (4,	4, '{6,10}', 14.40),
            (5,	4, '{4}', 7.00),
            (6,	5, '{5}', 65000.00),
            (7,	6, '{3,8,9}', 326.19),
            (8,	7, '{1,2,7,10}', 11.70)
                """)
    
    # INSERT STORAGE_INFO
    cur.execute("""
        INSERT INTO storage_info (item_id, amount, location) VALUES 
            (1,	11, 'Finland'),
            (2,	7, 'Sweden'),
            (3,	4, 'Finland'),
            (4,	60, 'Finland'),
            (5,	1, 'Finland'),
            (6,	68, 'Finland'),
            (7,	7, 'Finland'),
            (8,	32, 'Finland'),
            (9,	54, 'Finland'),
            (10, 200, 'Finland')
                """)
    
    cur.close()
    conn.close()

dbInit()
print("Databases created and populated")