import os
# os.remove("deleted_file.txt")
# os.rename("rename_file.txt", "new_raname_file.txt")
# os.rmdir("new_dir")
# os.mkdir("new_dir")
# file = open("file.txt", "a")
# with open("путь_к_файлу.txt", "r", encoding="utf-8") as f:

try:
 file = open("file.txt", "w", encoding="utf-8")
 try:
    file.write("Мой новый текст")
 except Exception as error:
    print(error)
 finally:
    print("Закрываем файл")
    file.close()
except FileNotFoundError as error:
    print(error)

with open("путь_к_файлу.txt", "w", encoding="utf-8") as f:
 f.write("Мой новый текст")
