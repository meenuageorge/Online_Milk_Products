from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    name = models.TextField()
    breed = models.TextField()
    eartag = models.TextField()
    age = models.TextField()
    type = models.TextField()
    weight = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Vaccine(models.Model):
    date_of_vaccination=models.DateField()

    def __str__(self):
        return self.date_of_vaccination

class Eartag(models.Model):
    type = models.TextField()
    previoustag = models.TextField()

    def __str__(self):
        return self.type

class NewEartag(models.Model):
    name = models.TextField()
    type = models.TextField()
    age = models.TextField()



    def __str__(self):
        return self.name

class MilkRecord(models.Model):
    name = models.TextField()
    userid = models.TextField()
    address = models.TextField()
    date = models.DateField()
    morning_milk_record=models.TextField()
    evening_milk_record = models.TextField()
    payment = models.TextField()


    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)

    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    def get_id(self):
        return str('%s (%s)' % (self.user.id))

    def _str_(self):
        return self.user.first_name

class Product(models.Model):
    name = models.CharField(max_length=40)
    product_image = models.ImageField(upload_to='product_image/')
    price = models.PositiveIntegerField()
    quantity = models.CharField(max_length=40)

    def _str_(self):
        return self.name

class Orders(models.Model):

    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
    email = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=500, null=True)
    mobile = models.CharField(max_length=20, null=True)
    order_date = models.DateField(auto_now_add=True, null=True)