from django.conf.urls import url
from model_forms_app import views

urlpatterns = [
    # grabs the rendered users function from views.py
    url(r'^$', views.users, name='users'),
]