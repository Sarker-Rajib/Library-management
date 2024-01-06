from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book

# Create your views here.
class BookDetails(DetailView):
    model = Book
    template_name = 'book/bookDetails.html'
    pk_url_kwarg = 'id'