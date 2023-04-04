from .models import *
from django.forms import ModelForm, TextInput, EmailInput, Select, FileInput, HiddenInput
class ArticlesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ArticlesForm, self).__init__(*args, **kwargs)
        self.fields['op'].empty_label = 'Направление не выбрано'
        self.fields['course'].empty_label = 'Курс не выбран'
    class Meta:
        model = Articles
        fields = ['number', 'mail', 'name', 'op', 'course', 'project_name', 'teach_name', 'phone', 'dmodel', 'note', 'comment', 'status']
        exclude = ['comment', 'status']
        widgets = {
            "number": TextInput(attrs={
                'class': 'form-control',
                'readonly': 'True',
                'required': 'True'
            }),
            "mail": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Электронная почта',
                'required': 'True'
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия Имя Отчество',
                'required': 'True'
            }),
            "op": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Образовательная программа',
                'required': 'True'
            }),
            "course": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Курс',
                'required': 'True'
            }),
            "project_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название проекта/КР/ВКР',
                'required': 'True'
            }),
            "teach_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО Научного руководителя',
                'required': 'True'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон',
                'required': 'True'
            }),
            "dmodel": FileInput(attrs={
                'class': 'form-control',
                'placeholder': '3D модель',
                'aria-label' : 'file example',
                'required': 'True'
            }),
            "note": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Скан служебной записки',
                'required': 'True'
            }),
            "comment": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий к заявке',
                'required': 'True'
            }),
            "status": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Статус',
                'required': 'True'
            }),
        }
