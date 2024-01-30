from django.db import models


# Create your models here.
class Services (models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date= models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_data']
class ContactUs (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()


    def __str__(self):
        return self.name
    


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Chief(models.Model):
    info = models.ForeignKey(CustomeUser , on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills)
    description = models.TextField()
    image = models.ImageField(upload_to='chief', default='chief.png')
    twitter = models.CharField(max_length=255, default='#')
    instagram = models.CharField(max_length=255, default='#')
    status = models.BooleanField(default=False)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.info.email
    
