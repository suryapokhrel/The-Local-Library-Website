from django.urls import URLPattern, include, path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('books/', views.BookListView.as_view(), name='books'),
]
