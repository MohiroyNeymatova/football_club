# Generated by Django 4.1.6 on 2023-11-08 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='first_team',
        ),
    ]
