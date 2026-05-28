import requests

# --- Часть 1: Базовый код из задания ---
print("--- Часть 1: Гарри Поттер ---")
url_harry = "https://openlibrary.org/search.json?q=harry+potter"
response = requests.get(url_harry)
data = response.json()

# Выводим название первой книги
first_book_title = data['docs'][0]['title']
print(f"Первая книга по запросу 'Гарри Поттер': {first_book_title}")

print("\n" + "=" * 30 + "\n")

# --- Часть 2 и 3: Другие книги и разная информация (Всё на русском) ---

# Список запросов (используем + вместо пробелов)
queries = [
    "the+great+gatsby",
    "war+and+peace",
    "1984+george+orwell"
]

# Словарь для перевода названий запросов (опционально, для красоты вывода)
query_names = {
    "the+great+gatsby": "Великий Гэтсби",
    "war+and+peace": "Война и мир",
    "1984+george+orwell": "1984"
}

for query in queries:
    display_name = query_names.get(query, query.replace('+', ' '))
    print(f"--- Поиск: {display_name} ---")
    url = f"https://openlibrary.org/search.json?q={query}"

    r = requests.get(url)
    book_data = r.json()

    if book_data['numFound'] > 0:
        doc = book_data['docs'][0]


        title = doc.get('title', 'Название не найдено')
        author = doc.get('author_name', ['Неизвестен'])[0]
        year = doc.get('first_publish_year', 'Не указан')
        pages = doc.get('number_of_pages_median', 'Нет данных')

        print(f"Название книги: {title}\n"
              f"Автор: {author}\n"
              f"Год публикации: {year}\n"
              f"Количество страниц: {pages}\n")
    else:
        print("Книги по данному запросу не найдены.")