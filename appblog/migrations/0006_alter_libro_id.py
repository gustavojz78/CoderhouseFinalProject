# Generated by Django 4.1.2 on 2022-11-07 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0005_rename_fechacreación_comentario_fechacreacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]