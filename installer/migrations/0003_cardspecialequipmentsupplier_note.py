# Generated by Django 3.1.5 on 2021-02-16 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('installer', '0002_remove_cardspecialequipmentsupplier_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardspecialequipmentsupplier',
            name='note',
            field=models.TextField(blank=True, null=True, verbose_name='Примечание'),
        ),
    ]
