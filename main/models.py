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
    

class Order(models.Model):
    name = models.CharField(max_length=50)
    surname= models.CharField(max_length=50)
    email = models.EmailField(("E-mail"), max_length=254)
    phone=models.CharField("Телефон",max_length=20)
    basket = models.TextField(("Корзина"))

    def __str__(self):
        return self.name +" " +self.surname