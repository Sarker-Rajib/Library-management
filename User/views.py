from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import CreateUserForm, DepositMoney
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from Books.models import Book
from .models import BorrowBook
from datetime import datetime


# Create your views here.
class CreateUser(FormView):
    form_class = CreateUserForm
    template_name = 'user/register-form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid.")
        return super().form_invalid(form)

class UserLoginView(LoginView):
    template_name = 'user/login-form.html'
    def get_success_url(self):
        return reverse_lazy('home')
    
class UserLogOUt(LogoutView):
    def get_success_url(self):
        return reverse_lazy('home')
    
class DepositMoneyView(FormView):
    form_class = DepositMoney
    template_name = 'user/deposit-form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.depositAccount

        account.balance += amount
        account.save(
            update_fields = ['balance']
        )
        return super().form_valid(form)

def profileView(request):
    user=request.user
    books = BorrowBook.objects.filter(borrowedBy=user)
    return render(request, 'user/profile.html', {'books':books, 'user':user})

def borrow_book(request, id):
    target_book = Book.objects.get(pk=id)
    price = target_book.borrowing_price
    account = request.user.depositAccount
    balance = account.balance

    if price > balance:
        messages.warning(request, "You dont have sufficient Money.")
        return redirect(f'/book/book-details/{id}')
    
    else:
        BorrowBook.objects.create(book=target_book, borrowedBy=request.user, currentBalance = balance - price)
        request.user.depositAccount.balance -= price
        request.user.depositAccount.save()
        return redirect('home')
    
def returnBook(request, id):
    borrowed_book = BorrowBook.objects.get(pk=id)
    price = borrowed_book.book.borrowing_price
    borrowed_book.returnTime = datetime.now()
    borrowed_book.returned = True
    borrowed_book.save()
    print(borrowed_book.returnTime)
    request.user.depositAccount.balance += price
    request.user.depositAccount.save()
    return redirect('profile')
