# Generated by Django 4.0 on 2022-01-19 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0060_card_caterogy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='caterogy',
            new_name='category',
        ),
    ]
