from django.db import models
from django.contrib.auth.models import User
from Books.models import Book

# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='depositAccount')
    account_no = models.IntegerField(unique=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.account_no}'

class BorrowBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    currentBalance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    timestamp= models.DateTimeField()
    returned = models.BooleanField(default=False)
    returnTime = models.DateTimeField(null=True)
    
    class Meta:
        ordering = ['timestamp']
    
    def __str__(self) -> str:
        return f'{self.book.title}'