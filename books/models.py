from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    book_image = models.ImageField(upload_to='book_images')
    seller_name = models.CharField(max_length=100, null=True, default=None)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return self.book_name
