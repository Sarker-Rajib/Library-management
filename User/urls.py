from django.urls import path
from .views import CreateUser, UserLogOUt, UserLoginView, DepositMoneyView

urlpatterns = [
    path('signup/', CreateUser.as_view(),name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogOUt.as_view(), name='logout'),
    path('deposit/', DepositMoneyView.as_view(), name='deposit'),
    # path('profile/', UserBankAccountUpdateView.as_view(), name='profile' )
]