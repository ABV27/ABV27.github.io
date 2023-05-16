from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Категория(models.Model):
    категория = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = 'Категории'
    def __str__(self):
        return self.категория

class Объявление(models.Model):
    категория = models.ForeignKey(Категория,on_delete=models.PROTECT)#нельзя удалить окуда есть записи
    товар = models.CharField(max_length=200)
    фото = models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)
    описание_товара = models.TextField(max_length=300)
    цена = models.FloatField(blank=True,)#хранит, значение типа Number, которое представляет число с плавающей точкой
    дата = models.DateTimeField(auto_now_add=True)
    wner = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    телефон = models.CharField(max_length=20)
    адрес = models.CharField(max_length=100)
    число = models.IntegerField(null=True)#хранит значение типа Number, которое представляет целочисленное значение
    class Meta:
        verbose_name_plural = 'Объявления'
        ordering = ['-дата']
    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.описание_товара[:50] + "..."
        
