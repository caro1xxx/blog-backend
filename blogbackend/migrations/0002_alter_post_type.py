# Generated by Django 3.2.7 on 2022-10-14 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogbackend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.TextField(verbose_name='tag'),
        ),
    ]