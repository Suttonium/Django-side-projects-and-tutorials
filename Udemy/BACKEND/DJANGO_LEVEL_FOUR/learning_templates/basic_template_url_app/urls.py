from django.conf.urls import url
from basic_template_url_app import views

# TEMPLATE TAGGING
app_name = 'basic_template_url_app'
urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other')
]