# Generated by Django 4.1.6 on 2023-11-09 19:40

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_delete_shopcollage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stadium',
            old_name='address',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='stadium',
            old_name='places',
            new_name='seats',
        ),
        migrations.RemoveField(
            model_name='stadium',
            name='images',
        ),
        migrations.RemoveField(
            model_name='stadium',
            name='texts',
        ),
        migrations.AddField(
            model_name='stadium',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.DeleteModel(
            name='StadiumImage',
        ),
        migrations.DeleteModel(
            name='StadiumText',
        ),
    ]