from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.create_user_info, name='create_user_info'),
]