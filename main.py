
print("\n" + "=" * 50)
print("КОМБИНИРОВАННЫЕ ЗАДАНИЯ")
print("=" * 50)
import random
random_list = [random.randint(1, 20) for _ in range(20)]
unique_values = list(set(random_list))
print(f"1. Случайный список: {random_list}")
print(f"   Уникальные значения: {unique_values}")

frequency_dict = {}
for num in random_list:
    if num in frequency_dict:
        frequency_dict[num] += 1
    else:
        frequency_dict[num] = 1
print(f"\n2. Частота элементов: {frequency_dict}")

words = ["программирование", "компьютер", "язык", "алгоритм", "код", "переменная"]
long_words = {word for word in words if len(word) > 5}
print(f"\n3. Список слов: {words}")
print(f"   Слова длиннее 5 символов: {long_words}")
sentence = input("\n4. Введите предложение: ")
word_count = {}
for word in sentence.split():
    word = word.strip('.,!?;:').lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(f"   Количество вхождений слов: {word_count}")

numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 5, 5, 5]
unique_numbers = list(set(numbers_with_duplicates))
print(f"\n5. Исходный список: {numbers_with_duplicates}")
print(f"   Без дубликатов: {unique_numbers}")

products = {
    "хлеб": 50,
    "молоко": 80,
    "сыр": 300,
    "колбаса": 250,
    "шоколад": 120
}
most_expensive = max(products, key=products.get)
print(f"\n6. Товары и цены: {products}")
print(f"   Самый дорогой товар: '{most_expensive}' за {products[most_expensive]} руб.")

names = ["анна", "иван", "мария", "иван", "петр", "анна", "мария", "мария"]
name_count = {}
for name in names:
    if name in name_count:
        name_count[name] += 1
    else:
        name_count[name] = 1

duplicate_names = [name for name, count in name_count.items() if count > 1]
most_common = max(name_count, key=name_count.get)

print(f"\n7. Список имён: {names}")
print(f"   Имена с повторами: {duplicate_names}")
print(f"   Самое частое имя: '{most_common}' ({name_count[most_common]} раз)")

text = input("\n8. Введите строку: ")
char_index = {}
for index, char in enumerate(text):
    if char not in char_index:
        char_index[char] = index
print(f"   Первые вхождения символов: {char_index}")