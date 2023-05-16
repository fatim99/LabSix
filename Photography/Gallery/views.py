from django.shortcuts import render
# Create baby views here.
def baby (request):
    return render(request, 'Gallery/baby.html')

# Create country views here.
def country (request):
    return render(request, 'Gallery/country.html')

# Create product views here.
def product (request):
    return render(request, 'Gallery/product.html')