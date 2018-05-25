from django.shortcuts import render
from lvl_two_app.models import User


# Create your views here.
def index(request):
    # renders the html files to the page
    return render(request, 'model_forms_app/thursday_list.html')


def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, 'model_forms_app/users.html', context=user_dict)
