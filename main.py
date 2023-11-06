import json

users = {}

while True:
    print('Введите следующие данные: ')
    first_name = input('Имя: ')
    last_name = input('Фамилию: ')

    user = {
        'first_name': first_name,
        'last_name': last_name,   
    }

    user_id = f'{last_name}.{first_name[0]}'

    users[user_id] = user

    choice = input('Добавить ещё пользователя? (Да/Нет): ')
    if choice.lower != 'Да':
        break

with open('users.json', 'w', encoding='utf-8') as file:
    json.dump(users, file, ensure_ascii=False)