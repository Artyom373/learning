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
