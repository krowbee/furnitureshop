from django.db import models

# Create your models here.

class Item(models.Model):
    
    slug= models.SlugField("Уникальное название",unique=True)
    title = models.CharField(("Название"), max_length=50)
    image = models.CharField(("Изображение"),max_length=50)
    desc = models.TextField(("Описание"))
    price = models.DecimalField("Цена",max_digits=5,decimal_places=2)

    def __str__(self):
        return self.title