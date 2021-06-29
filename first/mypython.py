# Работа над парсингом
#Настройка git
#test
# MASTER

#Цикл for
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for num in nums:
 print("Число: " + str(num))

for num in range(5):
     print("Число: " + str(num))

users = ["Mark", "Anna", "Maks", "Alex", "Roma"]
for user in users:
    print("Найден пользователь: " + user)
    if user == "Anna":
        print("Привет, " + user + "!")
        break

# Пропуск итерации цикла.
users = ["Mark", "Anna", "Maks", "Alex", "Roma"]
for user in users:
    if user == "Anna":
        continue
    print("Найден пользователь: " + user)

#Перебор элементов словар

user = {"name": "Mark", "phone": "+79518746317", "age": 23, "height": 182, "weight": 87}
for key in user:
 print(key)

user = {"name": "Mark", "phone": "+79518746317", "age": 23, "height": 182, "weight": 87}
for key in user:
 print(user[key])

# Перебор вложенных словарей
users = {
 "Mark": {"phone": "+79518746317", "age": 23, "height": 182, "weight": 87},
 "Anna": {"phone": "+79518746317", "age": 23, "height": 182, "weight": 87},
 "Oleg": {"phone": "+79518746317", "age": 23, "height": 182, "weight": 87},
 "Alex": {"phone": "+79518746317", "age": 23, "height": 182, "weight": 87},
}
for user_key in users:
 print()
 print("name: " + user_key)
 for user_attribute in users[user_key]:
    print(user_attribute + ": " + str(users[user_key][user_attribute]))

# Номер итерации в цикле for
users = ["Mark", "Anna", "Oleg", "Alex"]
for index, user in enumerate(users):
 print(str(index) +": " + user)

user = {"name": "Mark", "phone": "+795999568", "age": 25}
for key in user:
    print(key + ":" + str(user[key]))

print("Конец программы")

for key in user:
    try:
        print(key + ": " + user[key])
    except TypeError as exception:
        print(key + ": ", exception)

print("Конец программы")


user = {"name": "Mark", "phone": "+79507864598", "age": 25}
for key in user:
 try:
    print(key + ": " + user[key])
 except:
    print(key + ": ", "Ошибка!")
 finally:
    print("Этот блок сработает в любом случае")
    print("Конец программы")

# Форматирование через индексы
ref_link = "http://partner-cash.nu/ref/{ref_id}".format(ref_id=2194)
print(ref_link)

ref_link = "http://partner-cash.nu/ref/{0}".format(2194)
print(ref_link)

ref_link = "http://partner-cash.nu/{0}/{1}".format("mark", 2194)
print(ref_link)

word = "Строка"
glue = " / "
join_word = glue.join(word)
print(join_word)
# С / т / р / о / к / а

words = ["Раз", "Два", "Три", "Четыре", "Пять"]
glue = " / "
join_word = glue.join(words)
print(join_word)
# Раз / Два / Три / Четыре / Пять

words = "Lorem ipsum dolor sit amet consectetur adipiscing elit"
words_list = words.split(" ")
print(words_list)
# ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']

words = "Lorem ipsum dolor sit amet consectetur adipiscing elit"
words_list = words.split(" ", 3)
print(words_list)
# ['Lorem', 'ipsum', 'dolor', 'sit amet consectetur adipiscing elit']

num = "https://vk.com/id329483294"
is_vk_link = num.startswith("https://vk.com/id")
print(is_vk_link)
# True

story = "- Гуси-Гуси? \n-Га-га-га!"
dystopia = story.replace("Гуси", "Человеко", 1)
print(dystopia)
# - Человеко-Гуси? -Га-га-га!
1
