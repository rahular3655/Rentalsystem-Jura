from .views import *
from django.urls import path


urlpatterns = [
    path('categorylist',categoryList,name='categorylist'),
    path('addcategory',addcategory,name='addcategory'),
    path('productlist',product,name='productlist'),
    path('addproduct',addproduct,name='addproduct'),
    path('bookinglist',booking_list,name='bookinglist'),
    path('booking_create',booking_create,name='booking_create'),
]
