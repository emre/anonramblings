# Generated by Django 3.0.6 on 2020-05-17 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ramblings', '0009_post_reply_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment_count',
            field=models.IntegerField(default=0),
        ),
    ]