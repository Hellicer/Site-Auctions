# Generated by Django 4.0 on 2022-01-07 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_lot'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='comment',
            field=models.CharField(blank=True, max_length=244),
        ),
        migrations.AddField(
            model_name='card',
            name='price',
            field=models.FloatField(default=0, max_length=32),
        ),
        migrations.AlterField(
            model_name='lot',
            name='lot_price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lotPrice', to='auctions.card'),
        ),
        migrations.DeleteModel(
            name='Price',
        ),
    ]