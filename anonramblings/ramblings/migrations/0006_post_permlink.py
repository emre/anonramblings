# Generated by Django 3.0.6 on 2020-05-15 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ramblings', '0005_auto_20200515_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='permlink',
            field=models.CharField(default=1, max_length=36),
            preserve_default=False,
        ),
    ]
