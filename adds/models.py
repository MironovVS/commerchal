from django.db import models

# Create your models here.
class Advertising(models.Model):
    class Meta():
        db_table="Advertising"


    Advertising_header=models.CharField(max_length=200, verbose_name='Кратное описание')
    Advertising_text=models.TextField(verbose_name="Описание объявления")
    Advertising_date=models.DateTimeField(verbose_name="Дата публикации", auto_now_add=True)
    Advertising_price=models.IntegerField(default=0, verbose_name="Стоимость")

    def __str__(self):
        return self.Advertising_header

class Comments(models.Model):
    class Meta():
        db_table = "Comments"


    comments_text=models.TextField(verbose_name="Введите комментарий")
    comments_date=models.DateTimeField(verbose_name="Дата публикации", auto_now_add=True)
    comments_advertising=models.ForeignKey(Advertising)
