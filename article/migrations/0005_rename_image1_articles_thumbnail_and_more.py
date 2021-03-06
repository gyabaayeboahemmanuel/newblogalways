# Generated by Django 4.0 on 2022-03-14 12:58

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_rename_user_articles_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='image1',
            new_name='thumbnail',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='content_part1',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='content_part2',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='content_part3',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='content_part4',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='content_part5',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='content_part6',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='image5',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='image6',
        ),
        migrations.AddField(
            model_name='articles',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=1),
            preserve_default=False,
        ),
    ]
