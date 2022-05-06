# Generated by Django 4.0.4 on 2022-05-06 21:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 21, 17, 34, 551778), verbose_name='date published'),
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
        migrations.AddField(
            model_name='user',
            name='likes',
            field=models.ManyToManyField(to='blog.post'),
        ),
    ]