import json

try:
    with open('users.json', 'r', encoding='utf-8') as json_data:
        users = json.load(json_data)
except json.decoder.JSONDecodeError as err:
    users = {}
except FileNotFoundError:
    with open('users.json', 'w', encoding='utf-8') as file:
        users = json.load(file)


while True:
    print('Введите следующие данные: ')
    first_name = input('Имя: ')
    last_name = input('Фамилию: ')

    user = {
        'first_name': first_name,
        'last_name': last_name  
    }

    if 'users' not in users:
        users['users'] = []
    users['users'].append(user)

    choice = input('Добавить ещё пользователя? (Да/Нет): ')
    if choice.lower() in ['нет', 'no', 'n']:
        break

with open('users.json', 'w', encoding='utf-8') as file:
    json.dump(users, file, indent=4, ensure_ascii=False)