import requests

testForms = [
    # Три случая полного совпадения
    {
        'email': 'vra@mail.ru',
        'password': '1asf3151'
    },
    {
        'username': 'kirin',
        'email': 'vra@mail.ru',
        'phone': '+7 908 481 30 34',
        'birth_date': '2023-12-12',
    },
    {
        'articleTitle': 'Солнце',
        'articleText': 'Я вышел из дома',
        'date_released': '01.08.2004',
        'owner_email': 'email@mail.ru'
    },
    # Два случая неполного совпадения(в форме больше полей чем в шаблоне)
    {
        'email':'vra@mail.ru',
        'password': '1nasfnhioansag',
        'phoneNumber': '+7 908 481 30 34'
    },
    {
        'email':'vra@mail.ru',
        'password': '1nasfnhioansag',
        'code': '125asfas',
        'phoneNumber': '+7 908 481 30 34'
    },
    #Случаи с несоответсвием ни с одной формой
    {
        'username': 'kirin',
        'password': 'asgasgasg',
        'password_confirm': 'asfsagasg',
        'code': '1asgsa',
        'phoneNumber': '+7 908 481 30 34'
    },
    {
        'name': 'articleForm',
        'articleTitle': 'text',
        'articleText': 'text',
        'date_released': '20-10-2023',
        'owner_email': 'email'
    },
    {
        'username': 'kirin',
        'password': 'asgasgasg',
        'code': '1asgsa',
        'phoneNumber': '+79084813034'
    },
]

for form in testForms:
    response = requests.post('http://localhost:8000/get_form',data=form)
    print(response.json())