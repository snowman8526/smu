# Generated by Django 3.1.5 on 2021-02-16 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('installer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardspecialequipmentsupplier',
            name='note',
        ),
    ]