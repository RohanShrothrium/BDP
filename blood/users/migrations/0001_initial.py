# Generated by Django 2.1.2 on 2018-11-20 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_donated', models.DateField(default=django.utils.timezone.now)),
                ('about', models.TextField(default='Hey There!')),
                ('mobile_number', models.CharField(default='0836 2212842', max_length=14)),
                ('weight', models.CharField(default='69', max_length=3)),
                ('roll_number', models.CharField(default='NA', max_length=10)),
                ('blood_group', models.CharField(choices=[('A+', 'A+ve'), ('A-', 'A-ve'), ('B+', 'B+ve'), ('B-', 'B-ve'), ('O+', 'O+ve'), ('O-', 'O-ve'), ('AB+', 'AB+ve'), ('AB-', 'AB-ve')], default='A+', max_length=5)),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], default='MALE', max_length=10)),
                ('is_registered', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
