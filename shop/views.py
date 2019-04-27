from django.http import HttpResponse
from .models import Category , Product
# Create your views here.

def index(request):
    text_var = 'This is my first django webapp'
    return HttpResponse(text_var)