from django.db import models
from datetime import datetime

# Create your models here.

class BookCategory(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=80)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    image = models.ImageField(upload_to='books/media/images/')
    title = models.CharField(max_length = 45)
    description = models.TextField()
    borrowing_price = models.IntegerField()
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='feedbacks')
    name = models.CharField(max_length=20, blank=True)
    body = models.TextField(verbose_name='Your Feedback')
    created_on = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"Feedback by {self.name}"