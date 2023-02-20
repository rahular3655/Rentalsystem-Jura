from django.shortcuts import render,redirect
from .models import *
from accounts.views import * 
from django.contrib import messages
from django.forms import modelform_factory
from django.urls import reverse
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator


# Create your views here.

def categoryList(request):
    if 'username'in request.session:
        values = Categories.objects.all()
        return render(request,'categories.html',{'values':values})
    return redirect('signin')

def addcategory(request):
    values =Categories.objects.all()
    if request.method =='POST':
        name = request.POST.get('name')
        branch=request.POST.get('branch')
        slug = name.replace(" ","-").lower()
        variables = Categories(category_name=name,slug=slug,branch=branch)
        variables.is_available=True
        variables.save()
        return redirect(categoryList)
    return render(request,'Addcategory.html',{'values':values})


def product(request):
    theproduct = Product.objects.all()
    paginator = Paginator(theproduct, 5)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)
    return render(request,'product.html',{'theproduct':paged_product})

def addproduct(request):
    values = Categories.objects.all()
    if request.method =='POST':
        name = request.POST.get('name')
        tag = request.POST.get('tag')
        color = request.POST.get('color')
        size = request.POST.get('size')
        gender = request.POST.get('gender')
        catslug = name.replace(" ","-").lower()
        description = request.POST.get('description')
        price = request.POST.get('price')
        category = request.POST.get('category')
        image = request.FILES.get('image')
        x = Categories.objects.get(id=category)
        prod=Product(product_name=name,size=size,slug=catslug,gender=gender,Tag=tag,color=color,description=description,price=price,category=x,image=image)
        
        prod.save()
        
        
        return redirect(product)
    context = {
            'values':values,
        } 
    
    return render(request,'addproduct.html',context)


def booking_create(request):
    print(request)
    BookingForm = modelform_factory(Booking, exclude=['id'])

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            # Check if the product has already been booked in this date range
            existing_bookings = Booking.objects.filter(
                product=booking.product,
                booking_start_date__lte=booking.booking_end_date,
                booking_end_date__gte=booking.booking_start_date
            ).exclude(id=booking.id)
            if existing_bookings.exists():
                messages.error(request, 'This product has already been booked in this date range.')
                return redirect(reverse('booking_create'))

            booking.save()
            messages.success(request, 'Booking created successfully.')
            return redirect(reverse('bookinglist'))
    else:
        form = BookingForm()

    context = {
        'form': form,
    }
    return render(request, 'booking_create.html', context)



def booking_list(request):
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings,
    }
    return render(request, 'bookinglist.html', context)