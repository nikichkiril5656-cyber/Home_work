import sqlite3
from datetime import datetime, timedelta

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE departments (
    id INTEGER PRIMARY KEY,
    name TEXT,
    budget INTEGER
)
''')

cursor.execute('''
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department_id INTEGER,
    salary INTEGER,
    hire_date TEXT,
    FOREIGN KEY(department_id) REFERENCES departments(id)
)
''')

departments = [
    (1, 'IT', 50000),
    (2, 'HR', 30000),
    (3, 'Sales', 20000)
]
cursor.executemany('INSERT INTO departments VALUES (?, ?, ?)', departments)

today = datetime.now().strftime('%Y-%m-%d')
old_date = (datetime.now() - timedelta(days=4*365)).strftime('%Y-%m-%d')

employees = [
    (1, 'Alice', 1, 5000, old_date),
    (2, 'Bob', 1, 4000, today),
    (3, 'Charlie', 1, 6000, old_date),
    (4, 'David', 2, 3000, old_date),
    (5, 'Eve', 2, 2500, today),
    (6, 'Frank', 2, 3500, old_date),
    (7, 'Grace', 3, 2000, old_date),
    (8, 'Heidi', 3, 1000, today),
    (9, 'Ivan', 3, 2500, old_date),
    (10, 'Judy', 3, 1500, today)
]
cursor.executemany('INSERT INTO employees VALUES (?, ?, ?, ?, ?)', employees)
conn.commit()

print("--- Результаты запросов ---")

cursor.execute('''
SELECT d.name, SUM(e.salary) as total_salary
FROM employees e
JOIN departments d ON e.department_id = d.id
GROUP BY d.id
ORDER BY total_salary DESC
LIMIT 1
''')
res = cursor.fetchone()
print(f"3. Отдел с макс. суммарной зарплатой: {res[0]} (сумма: {res[1]})")

cursor.execute('''
SELECT e.name, e.salary, d.name
FROM employees e
JOIN departments d ON e.department_id = d.id
WHERE e.salary > (
    SELECT AVG(salary) 
    FROM employees e2 
    WHERE e2.department_id = e.department_id
)
''')
res = cursor.fetchall()
print("4. Сотрудники с зарплатой выше средней по отделу:")
for row in res:
    print(f"   - {row[0]} (Отдел: {row[2]}, ЗП: {row[1]})")

three_years_ago = (datetime.now() - timedelta(days=3*365)).strftime('%Y-%m-%d')
cursor.execute('SELECT name, hire_date FROM employees WHERE hire_date < ?', (three_years_ago,))
res = cursor.fetchall()
print("5. Сотрудники, работающие > 3 лет:")
for row in res:
    print(f"   - {row[0]} (нанят: {row[1]})")

cursor.execute('''
SELECT 
    d.name, 
    d.budget, 
    SUM(e.salary) as total_salary_expense,
    ROUND((SUM(e.salary) * 100.0 / d.budget), 2) as budget_percent
FROM departments d
JOIN employees e ON d.id = e.department_id
GROUP BY d.id
''')
res = cursor.fetchall()
print("6. Процент бюджета на зарплаты:")
for row in res:
    print(f"   - Отдел {row[0]}: Бюджет {row[1]}, Траты {row[2]}, Процент: {row[3]}%")

conn.close()