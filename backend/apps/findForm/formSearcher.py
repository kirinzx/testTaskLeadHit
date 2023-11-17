from .fieldTypes import detectFieldType, detectTemplateFieldType, Field
from typing import List
from pymongo import MongoClient
from decouple import config
from django.conf import settings


class TemplateForm:
    def __init__(self, formDict: dict):
        self.fields: List[Field] = []
        self.name = formDict.pop('name')
        for key, value in formDict.items():
            field = detectTemplateFieldType(key=key, value=value)
            if not field:
                raise TypeError('Не поддерживаемый тип')
            self.fields.append(field)

    def toDict(self) -> dict:
        form = {}
        for field in self.fields:
            form[field.key] = field.fieldTypeName
        return form

class CustomForm:
    def __init__(self, formDict: dict):
        self.fields: List[Field] = []
        for key, value in formDict.items():
            field = detectFieldType(key=key, value=value)
            if not field:
                raise TypeError('Не поддерживаемый тип')
            self.fields.append(field)

    def __eq__(self, other: TemplateForm):
        """
        Абсолютное равенство двух форм
        """
        if not isinstance(other, TemplateForm):
            return False
        
        if len(self.fields) != len(other.fields):
            return False
        
        for field in self.fields:
            foundField = self.findFieldByKey(field.key, other.fields)
            if not foundField:
                return False
            if field.fieldTypeName != foundField.fieldTypeName:
                return False

        return True
    
    def __sub__(self, other: TemplateForm) -> int:
        """
        Вычитание(Поля совпали, но в пришедшей форме полей больше). Возвращает кол-во одинаковых полей
        """
        count = 0

        if not isinstance(other, TemplateForm):
            return 0

        if len(self.fields) <= len(other.fields):
            return 0

        for field in other.fields:
            foundField = self.findFieldByKey(field.key, self.fields)
            if not foundField:
                return 0
            
            if field.fieldTypeName != foundField.fieldTypeName:
                return 0
            
            count += 1

        return count

        
    
    def findFieldByKey(self, key: str | int, fields: List[Field]) -> Field | None:
        for field in fields:
            if field.key == key:
                return field
            
    def toDict(self) -> dict:
        form = {}
        for field in self.fields:
            form[field.key] = field.fieldTypeName
        return form

class FormSearcher:
    def __init__(self, form: dict):
        self.mainForm = CustomForm(form)

    def findMatching(self) -> dict:
        db = settings.MONGOCLIENT[settings.MONGODB_DATABASE_NAME]
        collection = db[settings.MONGODB_DATABASE_COLLECTION]

        formsFound = collection.find({}, {'_id': False})

        almostMatchForm = {'count': 0, 'name': ''}

        for form in formsFound:
            templateForm = TemplateForm(form)

            if self.mainForm == templateForm:
                return {'name': templateForm.name}
            
            countOfMatchField = self.mainForm - templateForm
            if countOfMatchField:
                if almostMatchForm['count'] < countOfMatchField:
                    almostMatchForm['count'] = countOfMatchField
                    almostMatchForm['name'] = templateForm.name
        
        if almostMatchForm['name']:
            return {'name': almostMatchForm.get('name')}
        
        return self.mainForm.toDict()