from django.db import models
from accounts.models import CustomeUser

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Service(models.Model):
    title = models.CharField(max_length=100)
    content =models.CharField(max_length=200)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.title



class Menu(models.Model):
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='Menu',default='Menu.jpg')
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.title





class Events(models.Model):
    image = models.ImageField(upload_to='Event',default='Event.jpg')
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.title





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
    


class Skills(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Chefs(models.Model):
    info = models.ForeignKey(CustomeUser , on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    skills = models.ManyToManyField(Skills)
    image = models.ImageField(upload_to='trainer', default='teacher.png')
    twitter = models.CharField(max_length=255, default='#')
    facebook = models.CharField(max_length=255, default='#')
    instagram = models.CharField(max_length=255, default='#')
    linkdin = models.CharField(max_length=255, default='#')
    status = models.BooleanField(default=False)
    updated_datetime = models.DateTimeField(auto_now=True)
    


    def __str__(self):
        return self.info.email
    

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
    