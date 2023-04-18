from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('detail/<int:question_id>', views.detail_view, name="detail"),
    path('', views.index, name="index"),
    path('list/', views.viewlist, name="view_list"),
    path('<int:question_id>', views.vote, name = "vote")
]
