from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def products(request):
    return render(request,'products.html')

def products_details(request):
    return render(request,'products_details.html')



