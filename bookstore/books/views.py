from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from books.models import Book


def index(request):
    books = Book.objects.all()
    return render(request, "index.html" , {'books':books})