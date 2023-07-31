from django.shortcuts import render
from django.views import generic

# Создайте ваше отображение здесь

from .models import Book, Author, BookInstance, Genre


class BookListView(generic.ListView):
    """Generic class-based view for a list of books."""

    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""

    model = Book


class AuthorListView(generic.ListView):
    """Generic class-based view for a list of authors."""

    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    """Generic class-based detail view for an author."""

    model = Author


def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects

    num_books = Book.objects.count()  # The 'all()' is implied by default.
    num_instances = BookInstance.objects.count()
    # Available copies of books
    num_instances_available = BookInstance.objects.filter(status__exact="a").count()
    num_authors = Author.objects.count()
    # Homework
    num_genres_with_contain = Genre.objects.filter(name__icontains="fiction").count()
    num_books_with_contain = Book.objects.filter(title__icontains="the").count()

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        "index.html",
        context={
            "num_books": num_books,
            "num_instances": num_instances,
            "num_instances_available": num_instances_available,
            "num_authors": num_authors,
            "num_genres_with_contain": num_genres_with_contain,
            "num_books_with_contain": num_books_with_contain,
        },
    )
