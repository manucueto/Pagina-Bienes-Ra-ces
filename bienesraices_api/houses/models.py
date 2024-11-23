from django.db import models

# Create your models here.
class Houses(models.Model):
    house_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    rooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    parking = models.IntegerField()
    size = models.IntegerField()
    # image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Sellers(models.Model):
    seller_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class HousesSellers(models.Model):
    house_seller_id = models.AutoField(primary_key=True)
    house_id = models.ForeignKey(Houses, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(Sellers, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.house_id.title + ' - ' + self.seller_id.name