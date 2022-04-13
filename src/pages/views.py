from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    return render(request, 'home.html', {})

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})

def about_view(request, *args, **kwargs):
    my_context = {
        'my_text': 'This is about us',
        'my_number': 123,
        'my_list': {12,212,344,41313}
    }
    return render(request, 'about.html', my_context)

def products_view(request, *args, **kwargs):
    return render(request, 'products.html', {})