# Generated by Django 4.1.6 on 2023-11-09 11:46

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_delete_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='CLubPagePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Text Title')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
        migrations.RemoveField(
            model_name='achievementtext',
            name='achievements',
        ),
        migrations.DeleteModel(
            name='HistoryText',
        ),
        migrations.DeleteModel(
            name='Achievement',
        ),
        migrations.DeleteModel(
            name='AchievementText',
        ),
    ]
