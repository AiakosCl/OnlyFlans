# Generated by Django 4.2 on 2024-05-07 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_rename_contactform_contactos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='imagen',
            field=models.URLField(),
        ),
    ]
