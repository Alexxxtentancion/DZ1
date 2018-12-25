# Generated by Django 2.1.4 on 2018-12-24 07:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_book_users_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='users_like',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]