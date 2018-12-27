from django.conf import settings
from django.db import models
from django.urls import reverse


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(blank=False, null=False, max_length=100, verbose_name="Имя")
    patronymic = models.CharField(blank=True, max_length=50, verbose_name="Отчество")
    last_name = models.CharField(blank=True, max_length=100, verbose_name="Фамилия")
    date_of_birth = models.DateField(verbose_name="Дата рождения")

    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.patronymic, self.last_name)


class Book(models.Model):
    title = models.CharField(blank=False, null=False, max_length=100, verbose_name="Название")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")
    description = models.TextField(blank=True, verbose_name="Описание")
    photo = models.ImageField(upload_to='photo/%Y', default='/static/images/default.jpg', blank=True,
                              verbose_name="Фото")
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='book_liked', blank=True,
                                        verbose_name="Лайки")

    def get_absolute_url(self):
        return reverse('core:detail', args=[self.id])

    def __str__(self):
        return ' {}'.format(self.title)

    def get_like_url(self):
        return reverse("core:like-toggle", kwargs={"pk": self.pk})

    def get_api_like_url(self):
        return reverse("core:like-api-toggle", kwargs={"pk": self.pk})

    def get_book_url(self):
        return reverse("core:get-book", kwargs={"pk": self.pk})

    def get_api_book_url(self):
        return reverse("core:get-api-book", kwargs={"pk": self.pk})
