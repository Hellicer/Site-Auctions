# Generated by Django 4.0 on 2022-01-16 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0044_watchlist_lot'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlist',
            old_name='lot',
            new_name='card',
        ),
    ]
