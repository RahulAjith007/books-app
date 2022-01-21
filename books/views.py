from django.shortcuts import render
# from django.http import HttpResponse
import json

booksData = open(
    '/home/rahul/Projects/python/bookstore/books.json'
).read()

data = json.loads(booksData)

# Create your views here.
def index(request):
    context = {'books' : data}
    return render(request, 'books/index.html', context)


def show(request, id):
    book = None
    for singleBook in data:
        if (singleBook['id'] == id):
            book = singleBook
    context = {'book' : book}
    return render(request, 'books/show.html', context)