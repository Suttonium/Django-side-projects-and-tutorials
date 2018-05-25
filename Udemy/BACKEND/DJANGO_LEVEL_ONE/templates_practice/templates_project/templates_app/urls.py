from django.conf.urls import url
from templates_app import views

urlpatterns = [
    url(r'^$', views.help, name='help'),
]