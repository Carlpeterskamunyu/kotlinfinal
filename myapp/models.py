from django.db import models

# Create your models here.
class User(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    password = models.CharField(max_length=20)
    yob = models.DateField()

    def __str__(self):
        return self.fullname

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)  # CharField with max_length
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Using DecimalField for price
    quantity = models.IntegerField()  # IntegerField for quantity

    def __str__(self):
        return self.name


from django.db import models

class Appointments(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)  # Change to CharField for phone number
    datetime = models.DateTimeField()
    department = models.CharField(max_length=20)
    doctor = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name


from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

from django.contrib.auth.hashers import make_password

class Member(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)  # Enforce unique usernames
    password = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.pk:  # Hash password only on creation
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
