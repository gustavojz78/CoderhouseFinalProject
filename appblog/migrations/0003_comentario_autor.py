# Generated by Django 4.1.2 on 2022-10-12 03:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0002_alter_comentario_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='autor',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]