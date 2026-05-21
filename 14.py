import sqlite3

conn = sqlite3.connect('store.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS ORDER_ITEMS')
cursor.execute('DROP TABLE IF EXISTS ORDERS')
cursor.execute('DROP TABLE IF EXISTS PRODUCTS')
cursor.execute('DROP TABLE IF EXISTS CUSTOMERS')

cursor.execute('''
CREATE TABLE PRODUCTS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT NOT NULL,
    PRICE REAL NOT NULL,
    STOCK INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE CUSTOMERS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT NOT NULL,
    CITY TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE ORDERS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    CUSTOMER_ID INTEGER NOT NULL,
    ORDER_DATE DATE NOT NULL,
    FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMERS(ID)
)
''')

cursor.execute('''
CREATE TABLE ORDER_ITEMS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    ORDER_ID INTEGER NOT NULL,
    PRODUCT_ID INTEGER NOT NULL,
    QUANTITY INTEGER NOT NULL,
    FOREIGN KEY (ORDER_ID) REFERENCES ORDERS(ID),
    FOREIGN KEY (PRODUCT_ID) REFERENCES PRODUCTS(ID)
)
''')

cursor.execute("INSERT INTO PRODUCTS (NAME, PRICE, STOCK) VALUES ('Ноутбук Lenovo', 45000, 10)")
cursor.execute("INSERT INTO PRODUCTS (NAME, PRICE, STOCK) VALUES ('Мышь беспроводная', 1200, 50)")
cursor.execute("INSERT INTO PRODUCTS (NAME, PRICE, STOCK) VALUES ('Клавиатура механическая', 3500, 25)")
cursor.execute("INSERT INTO PRODUCTS (NAME, PRICE, STOCK) VALUES ('Монитор 24\"', 12000, 15)")

cursor.execute("INSERT INTO CUSTOMERS (NAME, CITY) VALUES ('Иван Петров', 'Москва')")
cursor.execute("INSERT INTO CUSTOMERS (NAME, CITY) VALUES ('Мария Сидорова', 'Санкт-Петербург')")
cursor.execute("INSERT INTO CUSTOMERS (NAME, CITY) VALUES ('Алексей Иванов', 'Новосибирск')")

cursor.execute("INSERT INTO ORDERS (CUSTOMER_ID, ORDER_DATE) VALUES (1, '2025-05-01')")
cursor.execute("INSERT INTO ORDERS (CUSTOMER_ID, ORDER_DATE) VALUES (2, '2025-05-15')")
cursor.execute("INSERT INTO ORDERS (CUSTOMER_ID, ORDER_DATE) VALUES (3, '2025-05-20')")

cursor.execute("INSERT INTO ORDER_ITEMS (ORDER_ID, PRODUCT_ID, QUANTITY) VALUES (1, 1, 1)")
cursor.execute("INSERT INTO ORDER_ITEMS (ORDER_ID, PRODUCT_ID, QUANTITY) VALUES (1, 2, 2)")
cursor.execute("INSERT INTO ORDER_ITEMS (ORDER_ID, PRODUCT_ID, QUANTITY) VALUES (2, 3, 1)")
cursor.execute("INSERT INTO ORDER_ITEMS (ORDER_ID, PRODUCT_ID, QUANTITY) VALUES (2, 2, 1)")
cursor.execute("INSERT INTO ORDER_ITEMS (ORDER_ID, PRODUCT_ID, QUANTITY) VALUES (3, 4, 2)")
cursor.execute("INSERT INTO ORDER_ITEMS (ORDER_ID, PRODUCT_ID, QUANTITY) VALUES (3, 2, 1)")

conn.commit()

print("=== ОБЩАЯ СУММА КАЖДОГО ЗАКАЗА ===")
cursor.execute('''
SELECT o.ID, c.NAME, SUM(p.PRICE * oi.QUANTITY) as total
FROM ORDERS o
JOIN CUSTOMERS c ON o.CUSTOMER_ID = c.ID
JOIN ORDER_ITEMS oi ON o.ID = oi.ORDER_ID
JOIN PRODUCTS p ON oi.PRODUCT_ID = p.ID
GROUP BY o.ID
''')
for row in cursor.fetchall():
    print(f"Заказ {row[0]}, {row[1]}: {row[2]} руб.")

print("\n=== ПОКУПАТЕЛИ, ПОТРАТИВШИЕ БОЛЕЕ 5000 РУБЛЕЙ ===")
cursor.execute('''
SELECT c.ID, c.NAME, SUM(p.PRICE * oi.QUANTITY) as total
FROM CUSTOMERS c
JOIN ORDERS o ON c.ID = o.CUSTOMER_ID
JOIN ORDER_ITEMS oi ON o.ID = oi.ORDER_ID
JOIN PRODUCTS p ON oi.PRODUCT_ID = p.ID
GROUP BY c.ID
HAVING total > 5000
''')
for row in cursor.fetchall():
    print(f"{row[1]}: {row[2]} руб.")

print("\n=== ТОВАРЫ, КОТОРЫЕ НИ РАЗУ НЕ ЗАКАЗЫВАЛИ ===")
cursor.execute('''
SELECT p.ID, p.NAME
FROM PRODUCTS p
LEFT JOIN ORDER_ITEMS oi ON p.ID = oi.PRODUCT_ID
WHERE oi.ID IS NULL
''')
for row in cursor.fetchall():
    print(f"{row[1]}")

print("\n=== САМЫЙ ПОПУЛЯРНЫЙ ТОВАР (ПО КОЛИЧЕСТВУ ПРОДАЖ) ===")
cursor.execute('''
SELECT p.ID, p.NAME, SUM(oi.QUANTITY) as total_sold
FROM PRODUCTS p
JOIN ORDER_ITEMS oi ON p.ID = oi.PRODUCT_ID
GROUP BY p.ID
ORDER BY total_sold DESC
LIMIT 1
''')
row = cursor.fetchone()
print(f"{row[1]}: продано {row[2]} шт.")

conn.close()

# ЧАСТЬ 2: АНАЛИЗ ТЕКСТОВОГО ФАЙЛА
with open('text.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

total_lines = len(lines)
total_words = 0
longest_line = ''
max_length = 0

for line in lines:
    words = line.split()
    total_words += len(words)
    if len(line) > max_length:
        max_length = len(line)
        longest_line = line.strip()

print("\n=== АНАЛИЗ ФАЙЛА text.txt ===")
print(f"Общее количество строк: {total_lines}")
print(f"Общее количество слов: {total_words}")
print(f"Самая длинная строка ({max_length} символов): {longest_line}")