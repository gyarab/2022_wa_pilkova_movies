# Generated by Django 4.1.7 on 2023-05-09 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0005_rename_genre_movie_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]