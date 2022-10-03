from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(), name='list'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]