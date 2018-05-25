from django.conf.urls import url
from lvl_two_app import views

urlpatterns = [
    # grabs the rendered users function from views.py
    url(r'^$', views.users, name='users'),
]