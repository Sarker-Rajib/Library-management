from django.urls import path
from .views import BookDetails

urlpatterns = [
    path('book-details/<int:id>', BookDetails.as_view(), name='bookDetails')
]