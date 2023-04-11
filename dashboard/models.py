from django.db import models
from django.contrib.auth.models import User
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
# Create your models here.
category=(
    ('stationary','stationary'),
    ('electronics','electronics'),
    ('non-technical','non-technical'),
)
class Product(models.Model):
    asset=models.CharField(max_length=30,null=True)
    sno=models.CharField(max_length=15,null=True)
    name=models.CharField(max_length=100,null=True)
    category=models.CharField(max_length=20,choices=category,null=True)
    quantity=models.PositiveIntegerField(null=True)
    model=models.CharField(max_length=300,null=True)
    barcode=models.ImageField(upload_to='images/',null=True)
    price=models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural='Product'
    
    def __str__(self) -> str:
        return f'{self.name}-{self.quantity}'
    
    def save(self,*args,**kwargs):
        EAN=barcode.get_barcode_class('ean13')
        ean=EAN(f'{self.asset}',writer=ImageWriter())
        buffer=BytesIO()
        ean.write(buffer)
        self.barcode.save('barcode.png',File(buffer),save=False)
        return super().save(*args,**kwargs)
    


class Issued_Items(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    staff=models.ForeignKey(User,models.CASCADE,null=True)
    issueditem_quantity=models.PositiveIntegerField(null=True)
    date=models.DateTimeField(auto_now_add=True)
    location=models.CharField(max_length=50,null=True)
    
    class Meta:
        verbose_name_plural='Issued_Items'

    def __str__(self) -> str:
        return f'{self.product} issued to {self.staff}'

