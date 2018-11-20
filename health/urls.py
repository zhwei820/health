try:
    from django.urls import path
except Exception as e:
    from django.conf.urls import url as path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
