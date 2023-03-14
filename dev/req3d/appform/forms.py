from .models import Articles
from django.forms import ModelForm, TextInput, EmailInput, Select, FileInput, HiddenInput
class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['number', 'mail', 'name', 'op', 'course', 'project_name', 'teach_name', 'phone', 'dmodel', 'note', 'comment', 'status']
        exclude = ['comment', 'status']
        widgets = {
            "number": TextInput(attrs={
                'class': 'form-control',
                'readonly': 'True',
                'required': ''
            }),
            "mail": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Электронная почта',
                'required': ''
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия Имя Отчество',
                'required': ''
            }),
            "op": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Образовательная программа',
                'required': ''
            }),
            "course": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Курс',
                'required': ''
            }),
            "project_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название проекта/КР/ВКР',
                'required': ''
            }),
            "teach_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО Научного руководителя',
                'required': ''
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон',
                'required': ''
            }),
            "dmodel": FileInput(attrs={
                'class': 'form-control',
                'placeholder': '3D модель',
                'aria-label' : 'file example',
                'required': ''
            }),
            "note": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Скан служебной записки',
                'required': ''
            }),
            "comment": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий к заявке',
                'required': ''
            }),
            "status": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Статус',
                'required': ''
            }),
        }
