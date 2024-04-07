from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import *

import json

from books.models import Book

# Create your views here.
def hello(request):
    print(request)
    return HttpResponse("hellooooo")




books=[
    {"id":1 , "title":"book1", "no_of_page":150, "author":"auth1", "price":90,
 "image":"pic1.jpg"},
 {"id":2 , "title":"book2", "no_of_page":200, "author":"auth2", "price":150,
 "image":"pic2.jpg"},
 {"id":3 , "title":"book3", "no_of_page":250, "author":"auth3", "price":200,
 "image":"pic3.jpg"}

]

def AllBooks(request):
    return render(request,"books/home.html",
                  context={"books":books})


def bookProfile(request,id):
    filter_books=filter(lambda book:book['id'] == id,books)
    filter_books=list(filter_books)
    if filter_books:
        book=filter_books[0]
        return render(request,"books/show.html",
                  context={"book":book})

def empty(request):
    return render(request,"books/empty.html")

def showAllBooks(request):
    books = Book.objects.all()
    return render(request,'books/home.html',context={'books':books}) 

def showBook(request,id):
    book=get_object_or_404(Book,pk=id)
    return render(request,'books/show.html',context={'book':book})

def deleteBook(request,id):
    book=get_object_or_404(Book,pk=id)
    book.delete()
    url = reverse('books.home')
    return redirect(url)

def createBook(request):
    if request.method=='POST':
        if request.FILES:
            image = request.FILES['image']
        else:
            image = None
        book = Book(title=request.POST['title'],price=request.POST['price'],no_of_page=request.POST['no_of_page'],author=request.POST['author'],image=image)
        
        book.save()
        return redirect(book.show_url)

    return render(request,'books/create.html')

def updateBook(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.no_of_page = request.POST.get('no_of_page')
        book.price = request.POST.get('price')
        book.author = request.POST.get('author')
        if request.FILES.get('image'):
            book.image = request.FILES['image']

        book.save()
        return redirect(book.show_url) 
  
    return render(request, 'books/update.html', {'book': book})



def book_create_form(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST,request.FILES)
    
        if form.is_valid():
            book = Book(title=form.cleaned_data['title'],price=form.cleaned_data['price'],no_of_page=form.cleaned_data['no_of_page'],author=form.cleaned_data['author'],image=form.cleaned_data['image'])
            book.save()
            return redirect(book.show_url)
    else:
        form = BookForm()

    return render(request, "books/forms/create.html", context={"form": form})




def create_book_model_form(request):
    form = BookModelForm()
    if request.method == "POST":
        form = BookModelForm(request.POST, request.FILES)
        if form.is_valid():
            book=form.save()
            return redirect(book.show_url)

    return render(request, 'books/forms/createmodelform.html',
                  context={"form": form})


def edit_book(request,id):
    book= Book.get_book_by_id(id) 
    form = BookModelForm(instance=book)
    if request.method == "POST":
        form = BookModelForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect(book.show_url)
    return render(request, 'books/forms/edit.html',
              context={"form": form})