# Generated by Django 4.1.2 on 2022-11-17 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0011_alter_comentario_texto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='texto',
            field=models.CharField(max_length=5000),
        ),
    ]