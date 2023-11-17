import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.conf import settings

db = settings.MONGOCLIENT[settings.MONGODB_DATABASE_NAME]
collection = db[settings.MONGODB_DATABASE_COLLECTION]

forms = [
    {
        'name': 'loginForm',
        'email': 'email',
        'password': 'text'
    },
    {
        'name': 'signUpForm',
        'username': 'text',
        'email': 'email',
        'phone': 'phone',
        'birth_date': 'date',
    },
    {
        'name': 'loginForm2',
        'email': 'email',
        'password': 'text',
        'code': 'text'
    },
    {
        'name': 'articleForm',
        'articleTitle': 'text',
        'articleText': 'text',
        'date_released': 'date',
        'owner_email': 'email'
    }
]

collection.insert_many(forms)