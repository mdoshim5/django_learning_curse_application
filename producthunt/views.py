from datetime import datetime
from math import prod
from django.shortcuts import redirect, render, get_object_or_404
from .models import Product
from django.contrib.auth.decorators import login_required

def home(request):
    products = Product.objects
    return render(request, 'producthunt/home.html', {'products':products})

def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if product is not None:
        return render(request, 'producthunt/detail.html', {'product':product})
    else:
        return render(request, 'producthunt/home.html')

@login_required
def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        icon = request.FILES['icon']
        image = request.FILES['image']
        if title and body and icon and image:
            product = Product()
            product.title = title
            product.body = body
            product.icon = icon
            product.image = image
            product.hunter = request.user
            product.publish_date = datetime.now()
            product.url = ''
            product.save()
            return redirect('producthunt')
        else:
            return render(request, 'producthunt/create.html', {'error': 'enter the fields and files correctly'})
    else:
        return render(request, 'producthunt/create.html')