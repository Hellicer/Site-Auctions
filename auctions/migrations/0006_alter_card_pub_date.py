# Generated by Django 4.0 on 2022-01-06 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_remove_card_image_alter_card_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='date published'),
        ),
    ]
