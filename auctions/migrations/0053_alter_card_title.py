# Generated by Django 4.0 on 2022-01-18 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0052_alter_rate_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='title',
            field=models.CharField(max_length=26, verbose_name='lot-input'),
        ),
    ]
