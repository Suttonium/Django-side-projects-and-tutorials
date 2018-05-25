from django.shortcuts import render
from forms_app import forms


# Create your views here.
def index(request):
    return render(request, 'forms_app/thursday_list.html')


def form_page(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # do something
            print('VALIDATION_SUCCESS')
            print('NAME: ' + form.cleaned_data['name'])
            print('EMAIL: ' + form.cleaned_data['email'])
            print('TEXT: ' + form.cleaned_data['text'])

    return render(request, 'forms_app/form_page.html', {'form': form})
