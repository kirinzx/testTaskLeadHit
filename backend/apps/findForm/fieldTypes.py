import re
from datetime import datetime

class Field:
    def __init__(self, key: str | int, value: str):
        self.key = key
        self.value = value
        self._is_valid = self.validate()

    def validate(self) -> bool:
        if not self.value:
            return False
        
        if not self.key:
            return False

        if not isinstance(self.value, str):
            return False
        
        if not (isinstance(self.key, int) or isinstance(self.key, str)):
            return False
        
        return True
    
    @property
    def is_valid(self):
        return self._is_valid

class EmailField(Field):
    __PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    fieldTypeName = 'email'
    def __init__(self, key, value):
        super().__init__(key, value)

    def validate(self) -> bool:
        if not super().validate():
            return False
        
        if not re.match(self.__PATTERN,self.value):
            return False
        
        return True

class PhoneField(Field):
    __PATTERN = r'^\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}$'
    fieldTypeName = 'phone'
    def __init__(self, key, value):
        super().__init__(key, value)

    def validate(self) -> bool:
        if not super().validate():
            return False
        
        if not re.match(self.__PATTERN,self.value):
            return False
        
        return True

class DateField(Field):
    __PATTERN_1 = '%d.%m.%Y'
    __PATTERN_2 = '%Y-%m-%d'
    fieldTypeName = 'date'
    def __init__(self, key, value):
        super().__init__(key, value)

    def validate(self) -> bool:
        if not super().validate():
            return False
        
        try:
            tmp = datetime.strptime(self.value, self.__PATTERN_1)
        except ValueError:
            try:
                tmp = datetime.strptime(self.value, self.__PATTERN_2)
            except ValueError:
                return False
        
        return True

class TextField(Field):
    fieldTypeName = 'text'
    def __init__(self, key, value):
        super().__init__(key, value)

def detectFieldType(key: str | int, value: str) -> EmailField | PhoneField | DateField | TextField | None:
    dateField = DateField(key=key, value=value)

    if dateField.is_valid:
        return dateField
    
    phoneField = PhoneField(key=key, value=value)

    if phoneField.is_valid:
        return phoneField

    emailField = EmailField(key=key, value=value)

    if emailField.is_valid:
        return emailField

    textField = TextField(key=key, value=value)

    if textField.is_valid:
        return textField
    
def detectTemplateFieldType(key: str | int, value: str) -> EmailField | PhoneField | DateField | TextField | None:
    if value == 'email':
        return EmailField(key, 'vr@mai.ru')
    
    if value == 'phone':
        return PhoneField(key, '+7 999 999 99 99')
    
    if value == 'date':
        return DateField(key, '2000-08-10')
    
    return TextField(key, 'something')