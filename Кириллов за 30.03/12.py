# Задание 1
filename = 'data.txt'
output_filename = 'corrected_data.txt'

items = {}

with open(filename, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    if not line: continue

    if ',' in line:
        parts = line.split(',')
        if len(parts) == 2:
            product_name = parts[0].strip()
            quantity = int(parts[1].strip())
            if product_name in items:
                items[product_name] += quantity
            else:
                items[product_name] = quantity


with open(output_filename, 'w', encoding='utf-8') as f:
    for product, total in items.items():
        f.write(f"{product}, {total}\n")

if items:
    total_products = sum(items.values())
    most_popular_product = max(items, key=items.get)

    print(total_products)
    print(most_popular_product)


# Задание 2
filename = 'text.txt'

with open(filename, 'r', encoding='utf-8') as f:
    lines = f.readlines()

total_lines = len(lines)
total_words = 0
longest_line = ""
longest_line_length = 0

for line in lines:
    clean_line = line.strip()
    words = clean_line.split()
    total_words += len(words)

    current_line_content = line.rstrip('\n')
    current_length = len(current_line_content)

    if current_length > longest_line_length:
        longest_line_length = current_length
        longest_line = current_line_content

print(total_lines)
print(total_words)
print(longest_line)