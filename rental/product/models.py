from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

# Create your models here.

class Categories(models.Model):
    category_name = models.CharField(max_length = 50,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    branch=models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.category_name
    
    
class Product(models.Model):
    product_name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    Tag=models.CharField(max_length=50,null=True)
    color=models.CharField(max_length=50,null=True)
    size=models.CharField(max_length=50,null=True)
    description=models.TextField(max_length=100,null=True)
    gender=models.CharField(max_length=15,null=True)
    price = models.FloatField(validators=[MinValueValidator(0)])
    is_available = models.BooleanField(default=True)
    is_booked=models.BooleanField(default=False)
    discount = models.IntegerField(null= False, default= 0 )
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/products')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.product_name
    
class Booking(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    booking_start_date = models.DateField()
    booking_end_date = models.DateField()
    customer_name=models.CharField(max_length=100,null=True)
    phonenumber=models.CharField(max_length=12,null=True)
    whp_nmbr = models.CharField(max_length=12,null=True)
    reference_no=models.CharField(max_length=10,null=True)
    shop=models.ForeignKey(Categories,null=True,on_delete=models.CASCADE)
    seller=models.CharField(max_length=20,null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['product', 'booking_start_date', 'booking_end_date'], name='unique_booking')
        ]

    def clean(self):
        super().clean()
        bookings = Booking.objects.filter(product=self.product, booking_start_date__lte=self.booking_end_date, booking_end_date__gte=self.booking_start_date)
        if self.id:
            bookings = bookings.exclude(id=self.id)
        if bookings.exists():
            raise ValidationError('This product has already been booked in this date range.')
        
    def __str__(self):
        return self.product.product_name

    