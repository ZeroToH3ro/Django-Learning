from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('add/', views.PostClass.as_view(), name='add'),
    path('save/', views.SaveNews.as_view(), name='save'),
    path('email', views.email_view, name='email'),
    path('process', views.process, name='process'),
    path('', views.IndexClass.as_view(), name='index'),

]
