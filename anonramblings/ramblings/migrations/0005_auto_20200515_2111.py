# Generated by Django 3.0.6 on 2020-05-15 21:11

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('ramblings', '0004_post_is_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=markdownx.models.MarkdownxField(max_length=5000),
        ),
    ]
