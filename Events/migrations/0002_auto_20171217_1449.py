# Generated by Django 2.0 on 2017-12-17 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='Description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='Event_Poster',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='Event_Speaker',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='Event_venue',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
