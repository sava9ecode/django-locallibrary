from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book, Author, BookInstance, Genre
from .forms import RenewBookForm
import datetime


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

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = 1 + num_visits

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
            "num_visits": num_visits,
        },
    )


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""

    model = BookInstance
    template_name = "catalog/bookinstance_list_borrowed_user.html"
    paginate_by = 10

    def get_queryset(self):
        return (
            BookInstance.objects.filter(borrower=self.request.user)
            .filter(status__exact="o")
            .order_by("due_back")
        )


class LoanedBooksAllListView(PermissionRequiredMixin, generic.ListView):
    """Generic class-based view listing all books on loan. Only visible to users with can_mark_returned permission."""

    model = BookInstance
    permission_required = "catalog.can_mark_returned"
    template_name = "catalog/bookinstance_list_borrowed_all.html"
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact="o").order_by("due_back")


@login_required
@permission_required("catalog.can_mark_returned", raise_exception=True)
def renew_book_librarian(request, pk):
    """View function for renewing a specific BookInstance by librarian"""
    book_instance = get_object_or_404(BookInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == "POST":
        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_instance.due_back = form.cleaned_data["renewal_date"]
            book_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse("all-borrowed"))

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={"renewal_date": proposed_renewal_date})

    context = {
        "form": form,
        "book_instance": book_instance,
    }

    return render(request, "catalog/book_renew_librarian.html", context)


class AuthorCreate(PermissionRequiredMixin, CreateView):
    model = Author
    fields = ["first_name", "last_name", "date_of_birth", "date_of_death"]
    initial = {"date_of_death": "2016-12-10"}
    permission_required = "catalog.can_mark_returned"


class AuthorUpdate(PermissionRequiredMixin, UpdateView):
    model = Author
    fields = ["first_name", "last_name", "date_of_birth", "date_of_death"]
    permission_required = "catalog.can_mark_returned"


class AuthorDelete(PermissionRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy("authors")
    permission_required = "catalog.can_mark_returned"


# Classes created for the forms challenge
class BookCreate(PermissionRequiredMixin, CreateView):
    model = Book
    fields = ["title", "author", "summary", "isbn", "genre", "language"]
    permission_required = "catalog.can_mark_returned"


class BookUpdate(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = ["title", "author", "summary", "isbn", "genre", "language"]
    permission_required = "catalog.can_mark_returned"


class BookDelete(PermissionRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy("books")
    permission_required = "catalog.can_mark_returned"
