from django.urls import path
from .views import CreateUser, UserLogOUt, UserLoginView, DepositMoneyView, profileView, borrow_book, returnBook

urlpatterns = [
    path('signup/', CreateUser.as_view(),name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogOUt.as_view(), name='logout'),
    path('profile/', profileView, name='profile' ),
    path('deposit/', DepositMoneyView.as_view(), name='deposit'),
    path('borrow-book/<int:id>', borrow_book, name='borrowBook'),
    path('return-book/<int:id>', returnBook, name='returnBook'),
]