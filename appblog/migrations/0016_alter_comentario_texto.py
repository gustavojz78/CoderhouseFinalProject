# Generated by Django 4.1.2 on 2022-11-17 02:55

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0015_alter_comentario_texto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='texto',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
