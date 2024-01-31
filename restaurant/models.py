from django.db import models
from accounts.models import CustomeUser


class Service(models.Model):
    title = models.CharField(max_length=100)
    content =models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Food(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    category = models.ManyToManyField(Category)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='Food/',default='defultjpg')
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class Party(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='Party/',default='defult.jpg')
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
class Order(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    number= models.IntegerField()
    message = models.TextField()
    date = models.DateTimeField()
    time= models.DateTimeField()
    def __str__(self):
        return self.email
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Chef(models.Model):
    name = models.CharField(max_length=100)
    info = models.ForeignKey(CustomeUser , on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill)
    image = models.ImageField(upload_to='Chef/', default='defult.jpg')
    instagram = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    linkdin = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.info.name

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    def __str__(self):
        return self.name
    