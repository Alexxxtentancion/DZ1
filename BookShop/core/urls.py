from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.BooksView.as_view(), name='list'),
    path('<int:pk>/like', views.BookLikeToggle.as_view(), name='like-toggle'),
    path('api/<int:pk>/like', views.BookLikeAPIToggle.as_view(), name='like-api-toggle'),
    path('<int:pk>/', views.BookDetail.as_view(), name='detail'),
    path('<int:pk>/get/', views.BookGet.as_view(), name='get-book'),
    path('my_books/', views.UsersBooks.as_view(), name='get-book'),
    path('create/', views.BookCreateView.as_view(), name='book-create'),
    path('<int:pk>/update/', views.BookUpdateView.as_view(), name='book-create')
]
