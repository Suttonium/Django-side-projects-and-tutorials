from django.shortcuts import render
from django.http import HttpResponse

def help(request):
    help_dictionary = {'help_me': 'HELP PAGE'}
    return render(request, 'templates_app/help.html', context=help_dictionary)
