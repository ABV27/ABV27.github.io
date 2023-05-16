from django import forms
from .models import Объявление

class ОбъявлениеForm(forms.ModelForm):
    class Meta:
        model = Объявление
        fields = ("категория", "товар","фото","описание_товара","телефон","адрес", "цена")



