from django.db import models
from accounts.models import CustomeUser
import datetime



class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Menu(models.Model):
    image = models.ImageField(upload_to='Menu',default='Menu.jpg')
    title = models.CharField(max_length=100)
    detail = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    category = models.ManyToManyField(Category)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    
class Event(models.Model):
    image = models.ImageField(upload_to='Menu',default='Menu.jpg')
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    



class Skills(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Chefs(models.Model):
    info = models.ForeignKey(CustomeUser , on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    skills = models.ManyToManyField(Skills)
    image = models.ImageField(upload_to='trainer', default='teacher.png')
    status = models.BooleanField(default=False)
    updated_datetime = models.DateTimeField(auto_now=True)
    


    def __str__(self):
        return self.info.email
    


class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    number= models.IntegerField()
    message = models.TextField()
    date = models.DateTimeField()
    time= models.DateTimeField()

    def __str__(self):
        return self.email
    


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

