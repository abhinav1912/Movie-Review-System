# Generated by Django 3.0.5 on 2020-11-10 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_movie_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
