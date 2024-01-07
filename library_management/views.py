from django.shortcuts import render
from Books import models

def homepage(request, category_slug=None):
    books = models.Book.objects.all()
    category = models.BookCategory.objects.all()

    if category_slug is not None:
        filterOption = models.BookCategory.objects.get(slug = category_slug)
        books = models.Book.objects.filter(category = filterOption)
    # print(books)
    return render(request, 'index.html', {'books': books, 'category': category})