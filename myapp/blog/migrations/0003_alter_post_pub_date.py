# Generated by Django 4.0.4 on 2022-05-06 20:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_author_delete_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 20, 35, 16, 981137), verbose_name='date published'),
        ),
    ]
