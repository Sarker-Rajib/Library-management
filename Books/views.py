from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book
from .forms import FeedbackForm
from User.models import BorrowBook

# Create your views here.
class BookDetails(DetailView):
    model = Book
    template_name = 'book/bookDetails.html'
    pk_url_kwarg = 'id'

    def post(self, request, *args, **kwargs):
        review_form = FeedbackForm(data=self.request.POST)
        book = self.get_object()
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.name = f'{request.user.first_name} {request.user.last_name}'
            new_review.book = book
            new_review.save()
        return self.get(request, *args, **kwargs)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_feedback = self.object.feedbacks.all()
        review_form = FeedbackForm()
   
        context['reviews'] = all_feedback        
        context['review_form'] = review_form
        return context