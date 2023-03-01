from .models import Articles
from django.forms import ModelForm, TextInput, EmailInput, Select, FileInput, HiddenInput
class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['number', 'mail', 'name', 'op', 'course', 'project_name', 'teach_name', 'phone', 'dmodel', 'note', 'comment', 'status']
        exclude = ['comment', 'status']
        widgets = {
            "number": TextInput(attrs={
                'class': 'text',
                'readonly': 'True'
            }),
            "mail": EmailInput(attrs={
                'class': 'text',
                'placeholder': 'Электронная почта'
            }),
            "name": TextInput(attrs={
                'class': 'text',
                'placeholder': 'Фамилия Имя Отчество'
            }),
            "op": Select(attrs={
                'class': 'text',
                'placeholder': 'Образовательная программа'
            }),
            "course": Select(attrs={
                'class': 'text',
                'placeholder': 'Курс'
            }),
            "project_name": TextInput(attrs={
                'class': 'text',
                'placeholder': 'Название проекта/КР/ВКР'
            }),
            "teach_name": TextInput(attrs={
                'class': 'text',
                'placeholder': 'ФИО Научного руководителя'
            }),
            "phone": TextInput(attrs={
                'class': 'text',
                'placeholder': 'Телефон'
            }),
            "dmodel": FileInput(attrs={
                'class': 'text',
                'placeholder': '3D модель'
            }),
            "note": FileInput(attrs={
                'class': 'text',
                'placeholder': 'Скан служебной записки'
            }),
            "comment": TextInput(attrs={
                'class': 'text',
                'placeholder': 'Комментарий к заявке'
            }),
            "status": Select(attrs={
                'class': 'text',
                'placeholder': 'Статус'
            }),
        }
