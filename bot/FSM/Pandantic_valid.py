import re

from pydantic import BaseModel,validator,ValidationError


class ClientNameModel(BaseModel):
    name: str

    @validator('name')
    def validate_name(cls, value):
        if not re.match("^[а-яА-Я]+$", value):
            raise ValueError('Имя должно содержать только буквы')
        return value

class ClientSurnameModel(BaseModel):
    surname: str

    @validator('surname')
    def validate_surname(cls, value):
        if not re.match("^[а-яА-Я]+$", value):
            raise ValueError('Фамилия должна содержать только буквы')
        return value

class ClientPhoneModel(BaseModel):
    phone: str

    @validator('phone')
    def validate_phone(cls, value):
        if not re.match(r'^\+?[\d\s\-\(\)]{10,}$', value):
            raise ValueError('Номер телефона должен быть в правильном формате')
        return value