items = {}
with open('data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        name, count = line.strip().split(', ')
        count = int(count)
        if name in items:
            items[name] += count
        else:
            items[name] = count

with open('corrected_data.txt', 'w', encoding='utf-8') as f:
    for name, total in items.items():
        f.write(f"{name}, {total}\n")

total_goods = sum(items.values())

most_popular = ''
max_count = 0
for name, count in items.items():
    if count > max_count:
        max_count = count
        most_popular = name

print("Общее количество товаров:", total_goods)
print("Самый популярный товар:", most_popular)


with open('text.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

line_count = len(lines)

word_count = 0
for line in lines:
    word_count += len(line.split())

longest = ""
for line in lines:
    clean_line = line.strip()
    if len(clean_line) > len(longest):
        longest = clean_line

print("Общее количество строк:", line_count)
print("Общее количество слов:", word_count)
print("Самая длинная строка:", longest)