from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100 , blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2 , blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey('auth.User', on_delete=models.CASCADE , related_name='products')

    def __str__(self):
        return f'Seller: {self.seller.username} / Product: {self.name} / Price: {self}'