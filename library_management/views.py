from django.shortcuts import render
from Books import models

def homepage(request):
    books = models.Book.objects.all()
    # print(books)
    return render(request, 'index.html', {'books': books})