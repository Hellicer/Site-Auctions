# Generated by Django 4.0 on 2022-01-10 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_remove_card_tag_lot_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='auctions.Card'),
        ),
    ]
