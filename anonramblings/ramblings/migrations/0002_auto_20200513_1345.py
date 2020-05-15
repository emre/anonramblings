# Generated by Django 3.0.6 on 2020-05-13 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ramblings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='ramblings.Tag'),
        ),
    ]
