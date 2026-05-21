import sqlite3
from datetime import date, timedelta

conn = sqlite3.connect('company.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    budget REAL NOT NULL
)
''')

cursor.execute('''
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department_id INTEGER NOT NULL,
    salary REAL NOT NULL,
    hire_date TEXT NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments(id)
)
''')

cursor.executemany(
    'INSERT INTO departments (name, budget) VALUES (?, ?)',
    [('IT', 500000.00), ('HR', 150000.00), ('Sales', 300000.00)]
)

employees_data = [
    ('Алексей Иванов', 1, 120000.00, '2022-01-15'),
    ('Мария Петрова', 1, 95000.00, '2023-03-10'),
    ('Дмитрий Сидоров', 1, 110000.00, '2021-11-20'),
    ('Елена Смирнова', 1, 130000.00, '2020-05-14'),
    ('Ольга Кузнецова', 2, 70000.00, '2019-08-01'),
    ('Иван Васильев', 2, 68000.00, '2022-12-01'),
    ('Павел Новиков', 3, 85000.00, '2023-06-15'),
    ('Анна Фёдорова', 3, 90000.00, '2021-09-20'),
    ('Сергей Морозов', 3, 78000.00, '2024-01-10'),
    ('Татьяна Волкова', 3, 88000.00, '2020-10-03')
]

cursor.executemany(
    'INSERT INTO employees (name, department_id, salary, hire_date) VALUES (?, ?, ?, ?)',
    employees_data
)

conn.commit()

cursor.execute('''
SELECT d.id, d.name, SUM(e.salary) as total_salary
FROM departments d
JOIN employees e ON d.id = e.department_id
GROUP BY d.id, d.name
ORDER BY total_salary DESC
LIMIT 1
''')
print("3. Отдел с максимальной суммарной зарплатой:", cursor.fetchone())

cursor.execute('''
SELECT e.id, e.name, e.salary, e.department_id
FROM employees e
JOIN (
    SELECT department_id, AVG(salary) as avg_salary
    FROM employees
    GROUP BY department_id
) dept_avg ON e.department_id = dept_avg.department_id
WHERE e.salary > dept_avg.avg_salary
''')
print("\n4. Сотрудники с зарплатой выше средней по отделу:")
for row in cursor.fetchall():
    print(f"   {row}")

three_years_ago = (date.today() - timedelta(days=3*365)).isoformat()
cursor.execute('''
SELECT id, name, department_id, hire_date,
       CAST((julianday('now') - julianday(hire_date)) / 365 AS INTEGER) as years_worked
FROM employees
WHERE hire_date <= ?
''', (three_years_ago,))
print("\n5. Сотрудники, работающие более 3 лет:")
for row in cursor.fetchall():
    print(f"   {row}")

cursor.execute('''
SELECT d.id, d.name, d.budget,
       COALESCE(SUM(e.salary), 0) as total_salary,
       ROUND((COALESCE(SUM(e.salary), 0) / d.budget) * 100, 2) as percentage
FROM departments d
LEFT JOIN employees e ON d.id = e.department_id
GROUP BY d.id, d.name, d.budget
''')
print("\n6. Процент бюджета отдела на зарплаты:")
for row in cursor.fetchall():
    print(f"   {row}")

conn.close()