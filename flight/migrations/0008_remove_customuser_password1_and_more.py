# Generated by Django 4.1.7 on 2023-03-18 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0007_customuser_password1_customuser_password2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='password2',
        ),
    ]
