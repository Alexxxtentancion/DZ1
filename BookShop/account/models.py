from django.conf import settings
from django.db import models
from core.models import Book


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,verbose_name="Юзер")
    date_of_birth = models.DateField(blank=True, null=True,verbose_name="Дата рождения")

    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True,verbose_name="Фото")
    my_books = models.ManyToManyField(Book, related_name='book_got', blank=True,verbose_name="Книги")

    def __str__(self):
        return '{}'.format(self.user.username)
