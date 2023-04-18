from django.contrib import admin
from django.urls import path, include
from .views import IndexClass, LoginClass, ViewUser, view_product

urlpatterns = [
    path('', IndexClass.as_view(), name='index'),
    path('login/', LoginClass.as_view(), name="login"),
    path('user-view/', ViewUser.as_view(), name="user-view"),
    path('product-view/', view_product, name="product-view")
]
