from django.shortcuts import render
from model_forms_app.forms import NewUser


# Create your views here.
def index(request):
    # renders the html files to the page
    return render(request, 'model_forms_app/thursday_list.html')


def users(request):
    form = NewUser()
    if request.method == 'POST':  # if someone submitted data
        form = NewUser(request.POST)
        if form.is_valid():  # if the data is valid
            form.save(commit=True)  # saves form to database
            return index(request)  # return back to homepage

    return render(request, 'model_forms_app/users.html', {'form':form})
