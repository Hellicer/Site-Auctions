# Generated by Django 4.0 on 2022-01-06 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_card_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='pub_date',
            field=models.DateField(auto_now_add=True, db_index=True),
        ),
    ]
