from django.contrib import admin

# Register your models here.
from .models import UserAccount, BorrowBook

admin.site.register(UserAccount)
admin.site.register(BorrowBook)