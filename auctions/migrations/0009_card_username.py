# Generated by Django 4.0 on 2022-01-07 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_rename_description_card_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='username',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]