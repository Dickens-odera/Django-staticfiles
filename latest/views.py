from django.shortcuts import render
from .models import Book
# Create your views here.
def latest_books(request):
 #book_list = Book.name.order_by('-pub_date')[:10]  
 #book_list = Book.objects.all().order_by('name') 
 return render(request,'books/index.html')