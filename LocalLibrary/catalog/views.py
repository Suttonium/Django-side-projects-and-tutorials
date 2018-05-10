from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from catalog.forms import UserForm
from .models import Author
from .models import Book
from .utils import *


class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listing books on loan to current user.
    """
    model = Book
    template_name = 'catalog/book_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Book.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


@login_required
def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    # Available books (status = 'a')
    num_books_available = Book.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # The 'all()' is implied by default.

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Render the HTML template thursday_list.html with the data in the context variable
    return render(
        request,
        'thursday_list.html',
        context={
            'num_books_available': num_books_available, 'num_authors': num_authors, 'num_visits': num_visits},
    )


class AuthorCreate(LoginRequiredMixin, CreateView):
    model = Author
    fields = '__all__'
    initial = {'date_of_death': '05/01/2018', }


class AuthorUpdate(LoginRequiredMixin, UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']


class AuthorDelete(LoginRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('authors')


class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Author


class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author


class UserFormView(View):
    form_class = UserForm
    template_name = 'catalog/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserForm()
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                user = User.objects.create_user(username=form.cleaned_data['username'],
                                                password=form.cleaned_data['password'],
                                                email=form.cleaned_data['email'])
                permission = Permission.objects.get(codename='delete_books')
                user.user_permissions.add(permission)
                user.save()
                new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                login(request, new_user)
                return redirect('index')
        return render(request, self.template_name, {'form': form})
