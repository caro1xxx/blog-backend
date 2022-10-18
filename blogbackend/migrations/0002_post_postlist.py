# Generated by Django 3.2.7 on 2022-10-18 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blogbackend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=32, unique=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=64)),
                ('type', models.TextField(verbose_name='tag')),
                ('content', models.TextField(verbose_name='内容')),
            ],
        ),
        migrations.CreateModel(
            name='PostList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=32, unique=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=64)),
                ('type', models.TextField(verbose_name='tag')),
                ('introduce', models.TextField(verbose_name='介绍')),
            ],
        ),
    ]