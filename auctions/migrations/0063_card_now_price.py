# Generated by Django 4.0 on 2022-01-27 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0062_card_checked'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='now_price',
            field=models.FloatField(blank=True, default=None, max_length=6, null=True),
        ),
    ]