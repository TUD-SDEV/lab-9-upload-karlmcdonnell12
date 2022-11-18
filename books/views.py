from django.views.generic import ListView, DetailView 
from .models import Book 
from django.db.models import Q

class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books.book_list.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
# Create your views here.

class SearchResultsListView(ListView):
    model = Book 
    contect_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self):
        query = self.request.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query))
        