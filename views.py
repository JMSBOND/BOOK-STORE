from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.db.models import Q


# Create your views here.
def welcome(request):
    return render(request, "Welcome.html")


def load_form(request):
    form = BookForm
    return render(request, "index.html", {'form': form})


def add(request):
    form = BookForm(request.POST)
    form.save()
    return redirect('/show')


def show(request):
    book = Book.objects.all
    return render(request, 'show.html', {'book': book})


def edit(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'edit.html', {'book': book})


def update(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST, instance=book)
    book = Book.objects.get(id=id)
    form.save()
    return redirect('/show')


def delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/show')




def search(request):
    give_name=request.POST['language']
    book = Book.objects.filter(Q(genre=give_name)| Q(language=give_name))
    return render(request, 'show.html', {'book': book})


