from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {'name' : 'Rahul'}
    return render(request, 'books/index.html', context)