# Generated by Django 4.0 on 2022-01-19 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0054_card_winner_alter_card_description_alter_card_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lotWinner', to='auctions.user'),
        ),
    ]
