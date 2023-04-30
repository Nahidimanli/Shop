from django.db import models

# Create your models here.

class AbstractBaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)


    class Meta:
        abstract = True

class Contact(AbstractBaseModel):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(max_length=200)
    

    def __str__(self):
        return self.name


class Fashion(AbstractBaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # catagory = models.ForeignKey(Catagory, related_name="names", on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return self.title
    

class Jewellery(AbstractBaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # catagory = models.ForeignKey(Catagory, related_name="names", on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return self.name
    

class Login(AbstractBaseModel):
    title = models.CharField(max_length=100)
    # catagory = models.ForeignKey(Catagory, related_name="names", on_delete=models.CASCADE)
   

    def __str__(self):
        return self.title
    

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)


class Home(models.Model):
    title = models.CharField(max_length=50)



class Electronic(models.Model):
    title = models.CharField(max_length=50)


