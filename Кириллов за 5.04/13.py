# Задание 1
import json

with open('students.json', 'r', encoding='utf-8') as file:
    students = json.load(file)

print("Список студентов и их средний балл:")
for student in students:
    print(f"{student['name']} - {student['gpa']}")


# Задание 2
with open('products.json', 'r', encoding='utf-8') as file:
    products = json.load(file)

filtered_products = [
    product for product in products
    if product['price'] > 1000 and product['in_stock'] is True
]

for product in filtered_products:
    product['discount'] = product['price'] * 0.1
    product['price'] = round(product['price'] * 0.9, 2)  # новая цена с 10% скидкой

print("Товары с ценой > 1000 и в наличии (после скидки 10%):")
for product in filtered_products:
    print(product)