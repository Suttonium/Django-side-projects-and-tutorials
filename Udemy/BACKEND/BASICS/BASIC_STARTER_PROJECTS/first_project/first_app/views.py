from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dictionary = {'insert_me': "Now I am coming from first_app/help.html"}  # matches variable created in thursday_list.html
    return render(request, 'first_app/thursday_list.html', context=my_dictionary)

