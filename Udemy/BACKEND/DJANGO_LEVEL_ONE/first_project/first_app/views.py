from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dictionary = {'insert_me': "Now I am coming from first_app/help.html"}  # matches variable created in index.
    return render(request, 'first_app/index.', context=my_dictionary)

