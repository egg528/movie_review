# Generated by Django 2.2.5 on 2021-01-21 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20210121_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='imdb_code',
            field=models.CharField(default='', max_length=100),
        ),
    ]
