import json
import datetime

try:
    with open('users.json', 'r', encoding='utf-8') as json_data:
        users = json.load(json_data)
except json.decoder.JSONDecodeError:
    users = {}
except (FileExistsError, OSError):
    with open('users.json', 'w', encoding='utf-8') as file:
        users = {}
        json.dump(users, file)

while True:
    print('Заполните следующие данные: ')
    first_name = input('Имя: ')
    last_name = input('Фамилию: ')
    birthday = input('Дата рождения (дд.мм.гггг): ')
    city = input('Город: ')
    address = input('Улица: ')

    b_day, b_month, b_year = birthday.split('.')
    street, house_num = address.replace(',', ' ').split()

    user = {
        'first_name': first_name,
        'last_name': last_name,
        'birthday': birthday,
        'address': {
            'city': city,
            'street': [street, house_num]
        }
    }

    if 'users' not in users:
        users['users'] = []
    users['users'].append(user)

    users['count'] = len(users['users'])

    choice = input('Добавить ещё пользователя? (Да/Нет): ')
    if choice.lower() in ['нет', 'no', 'n']:
        break

with open('users.json', 'r+', encoding='utf-8') as file:
    json.dump(users, file, indent=4, ensure_ascii=False)