# Generated by Django 3.0.6 on 2020-05-15 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ramblings', '0002_auto_20200513_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sent_to_blockchain',
            field=models.BooleanField(default=False),
        ),
    ]
