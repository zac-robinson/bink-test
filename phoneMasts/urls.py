from django.urls import path

from . import views


app_name = 'phoneMasts'
urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.upload_file, name='upload'),
    path('manual_upload', views.manual_upload, name='manual_upload'),
    path('sort', views.sort, name='sort'),
]
