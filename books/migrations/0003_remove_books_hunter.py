# Generated by Django 3.0.3 on 2020-03-07 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_books_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='hunter',
        ),
    ]
