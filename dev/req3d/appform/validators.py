from django.core.exceptions import ValidationError
import re
import os

def validate_name(value):
    if value is None:
        raise ValidationError("Не указано ФИО")
    if value.isdigit():
        raise ValidationError("ФИО может состоять только из букв")

def validate_phone(value):
    pattern = r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$'
    if not re.match(pattern, value):
        raise ValidationError("Неверный номер телефона, формат ввода: +7|8|7 9XXXXXXXXX")


def validate_mail(value):
    with open('appform/static/spam_emails.txt', 'r') as f:
        for line in f:
            if line.startswith(value):
                raise ValidationError("Спам почта")
    pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
    if not re.match(pattern, value):
        raise ValidationError("Неверный адрес электронной почты")

def validate_op(value):
    op = ["ИВТ","ИТСС","КБ","ПМ","ИБ","Другое"]
    if value not in op:
        raise ValidationError("Не заполнено поле образовательной программы")

def validate_course(value):
    courses = ['1 курс','2 курс','3 курс','4 курс','1 курс (магистратура)',
    '2 курс (магистратура)','Аспирантура','Сотрудник']
    if value not in courses:
        raise ValidationError("Не указана степень обучения")

def validate_project_name(value):
    if value is None:
        raise ValidationError("Не указано название проекта")

def validate_teach_name(value):
    if value is None:
        raise ValidationError("Не указано ФИО руководителя")
    if value.isdigit():
        raise ValidationError("ФИО может состоять только из букв")

def validate_dmodel(value):
    if not value.name.endswith(".stl"):
        raise ValidationError("Некорректный тип файла. Разрешён формат файла .stl")

def validate_note(value):
    ext = os.path.splitext(value.name)[1]  # get file extension
    valid_extensions = ['.pdf', '.doc', '.docx', '.txt']
    if not ext.lower() in valid_extensions:
        raise ValidationError("Некорректный тип файла. Разрешены .pdf, .doc, .docx и .txt")