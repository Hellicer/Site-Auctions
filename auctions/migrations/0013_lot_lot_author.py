# Generated by Django 4.0 on 2022-01-07 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_card_comment_card_price_alter_lot_lot_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lot',
            name='lot_author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='lotAuthor', to='auctions.user'),
        ),
    ]
