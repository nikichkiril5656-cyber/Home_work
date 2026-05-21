import sqlite3

# ЗАДАНИЕ 1
conn = sqlite3.connect('shop.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS CUSTOMERS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT NOT NULL,
    EMAIL TEXT UNIQUE NOT NULL,
    PHONE TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS PRODUCTS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT NOT NULL,
    PRICE REAL NOT NULL,
    STOCK INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS ORDERS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    CUSTOMER_ID INTEGER NOT NULL,
    PRODUCT_ID INTEGER NOT NULL,
    QUANTITY INTEGER NOT NULL,
    ORDER_DATE TEXT NOT NULL,
    FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMERS(ID),
    FOREIGN KEY (PRODUCT_ID) REFERENCES PRODUCTS(ID)
)
''')

conn.commit()

# ЗАДАНИЕ 2
def add_customer(name, email, phone):
    cursor.execute('INSERT INTO CUSTOMERS (NAME, EMAIL, PHONE) VALUES (?, ?, ?)', (name, email, phone))
    conn.commit()

def add_product(name, price, stock):
    cursor.execute('INSERT INTO PRODUCTS (NAME, PRICE, STOCK) VALUES (?, ?, ?)', (name, price, stock))
    conn.commit()

def place_order(customer_id, product_id, quantity, date):
    cursor.execute('INSERT INTO ORDERS (CUSTOMER_ID, PRODUCT_ID, QUANTITY, ORDER_DATE) VALUES (?, ?, ?, ?)',
                   (customer_id, product_id, quantity, date))
    cursor.execute('UPDATE PRODUCTS SET STOCK = STOCK - ? WHERE ID = ?', (quantity, product_id))
    conn.commit()

add_customer("Иван Петров", "ivan@mail.ru", "+7-999-123-4567")
add_customer("Мария Сидорова", "maria@mail.ru", "+7-999-234-5678")
add_customer("Алексей Иванов", "alex@mail.ru", "+7-999-345-6789")

add_product("Ноутбук", 45000, 15)
add_product("Мышь", 800, 30)
add_product("Клавиатура", 2500, 12)
add_product("Монитор", 12000, 8)
add_product("Наушники", 3500, 5)

place_order(1, 1, 1, "2024-01-15")
place_order(1, 2, 2, "2024-01-20")
place_order(2, 3, 1, "2024-01-18")
place_order(3, 5, 1, "2024-01-22")

# ЗАДАНИЕ 3
cursor.execute('''
SELECT ORDERS.ID, CUSTOMERS.NAME, PRODUCTS.NAME, ORDERS.QUANTITY, ORDERS.ORDER_DATE
FROM ORDERS
JOIN CUSTOMERS ON ORDERS.CUSTOMER_ID = CUSTOMERS.ID
JOIN PRODUCTS ON ORDERS.PRODUCT_ID = PRODUCTS.ID
''')
all_orders = cursor.fetchall()

cursor.execute('SELECT NAME, STOCK FROM PRODUCTS WHERE STOCK < 10')
low_stock = cursor.fetchall()

cursor.execute('''
SELECT CUSTOMERS.NAME, SUM(PRODUCTS.PRICE * ORDERS.QUANTITY)
FROM ORDERS
JOIN CUSTOMERS ON ORDERS.CUSTOMER_ID = CUSTOMERS.ID
JOIN PRODUCTS ON ORDERS.PRODUCT_ID = PRODUCTS.ID
GROUP BY CUSTOMERS.NAME
''')
customer_totals = cursor.fetchall()

def get_orders_by_customer(customer_id):
    cursor.execute('''
    SELECT ORDERS.ID, PRODUCTS.NAME, ORDERS.QUANTITY, ORDERS.ORDER_DATE
    FROM ORDERS
    JOIN PRODUCTS ON ORDERS.PRODUCT_ID = PRODUCTS.ID
    WHERE CUSTOMER_ID = ?
    ''', (customer_id,))
    return cursor.fetchall()

def update_product_stock(product_id, new_stock):
    cursor.execute('UPDATE PRODUCTS SET STOCK = ? WHERE ID = ?', (new_stock, product_id))
    conn.commit()

# ЗАДАНИЕ 4
cursor.execute('DELETE FROM PRODUCTS WHERE ID = 4')
conn.commit()

cursor.execute('UPDATE PRODUCTS SET PRICE = 50000 WHERE ID = 1')
conn.commit()

cursor.execute('SELECT ID, NAME, PRICE, STOCK FROM PRODUCTS')
updated_products = cursor.fetchall()

conn.close()