# Generated by Django 5.0.2 on 2024-02-17 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_tittle', models.CharField(max_length=30, verbose_name='Название статьи')),
                ('article_description', models.TextField(verbose_name='Текст статьи')),
                ('article_date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
    ]