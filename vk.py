# Открываем файл с аккаунтами
with open("path/to/file.txt") as f:
    # Разделяем файл на строки, каждую строку добавляем в список
    accounts = [account.rstrip('\n') for account in f]
for account in accounts:
    # Каждый аккаунт предствален в виде строки login:password
    # Разбиваем строку login:password на словарь со значениями
    # login и password и кладём их в переменные
    login, password = account.rstrip(':')
    try:
        # Получаем авторизационный ключ
        token = vk_api.auth(login, password)
        # Сохраняем этот ключ в "успешный" файл
        # login:password:token
        with open("path/to/success_file.txt") as f:
            f.write(login + ":" + password + ":" + token + "\n")
    except AuthFailed as ex:
        # Если авторизация не удалась - сохраняем аккаунт
        # в "неуспешный" файл
        with open("path/to/lose_file.txt") as f:
            f.write(login + ":" + password + ":" + ex + "\n")
    except:
        # Если произошла любая другая ошибка,
        # также сохраняем аккайнт в неуспешный файл
        with open("path/to/lose_file.txt") as f:
            f.write(login + ":" + password + ":" + "Неизвестная ошибка!" + "\n")

