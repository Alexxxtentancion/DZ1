from account.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, RedirectView

from .models import Book


# Create your views here.

class BooksView(ListView):
    template_name = 'core/list.html'
    queryset = Book.objects.all()
    context_object_name = 'books'


class UsersBooks(ListView):
    template_name = 'core/users_books_list.html'
    queryset = Profile.objects.all()
    context_object_name = 'users_books'

    def get(self, request, *args, **kwargs):
        user = self.request.user
        # pk =self.kwargs.get("pk")
        # obj1 = get_object_or_404(Profile,user=user)
        # obj2 = get_object_or_404(Book,pk=pk)
        # us_title =
        a=Profile.objects.filter(user=user)
        print([p.date_of_birth for p in a])
        return redirect('/core')


class BookDetail(DetailView):
    model = Book
    template_name = 'core/detail.html'


class BookLikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        pk = self.kwargs.get("pk")
        print(pk)
        obj = get_object_or_404(Book, pk=pk)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated:
            if user in obj.users_like.all():
                obj.users_like.remove(user)
            else:
                obj.users_like.add(user)
        return url_


class BookGet(LoginRequiredMixin, RedirectView):
    login_url = '/account/login/'

    def get_redirect_url(self, *args, **kwargs):
        pk = self.kwargs.get("pk")
        print(pk)
        obj = get_object_or_404(Book, pk=pk)
        url_ = obj.get_absolute_url()
        user = self.request.user
        obj_u = get_object_or_404(Profile, user=user)
        print(user, obj_u, obj)
        if user.is_authenticated:
            if obj not in obj_u.my_books.all():
                obj_u.my_books.add(obj)
        return url_


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions


class BookLikeAPIToggle(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk=None, format=None):
        # pk = self.kwargs.get("pk")
        obj = get_object_or_404(Book, pk=pk)
        url_ = obj.get_absolute_url()
        user = self.request.user
        updated = False
        liked = False

        if user.is_authenticated:
            if user in obj.users_like.all():
                liked = False
                obj.users_like.remove(user)
            else:
                liked = True
                obj.users_like.add(user)
            updated = True
        data = {
            "updated": updated,
            "liked": liked
        }
        return Response(data)
