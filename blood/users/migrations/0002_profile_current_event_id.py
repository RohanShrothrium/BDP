# Generated by Django 2.1.2 on 2018-11-27 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='current_event_id',
            field=models.IntegerField(default=0),
        ),
    ]
