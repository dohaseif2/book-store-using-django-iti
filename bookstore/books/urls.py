from django.urls import path
from books.views import *
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('home',showAllBooks,name='books.home'),
    path('<int:id>',showBook,name='books.show'),
    path('about',empty,name='books.about'),
    path('contact',empty,name='books.contact'),
    path('<int:id>/delete',login_required(deleteBook),name='books.delete'),
    path('create',createBook,name='books.create'),
    # path('<int:id>/update',updateBook,name='books.update'),
    path('forms/create',book_create_form,name='book.create.forms'),
    path('forms/createmodel', login_required(create_book_model_form), name='book.createmodel'),
    path('forms/<int:id>/edit',login_required(edit_book),name='books.update')
]
