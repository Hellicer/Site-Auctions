# Generated by Django 4.0 on 2022-01-19 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0057_card_close_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='lot_title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lotname', to='auctions.card'),
        ),
    ]
