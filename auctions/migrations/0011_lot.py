# Generated by Django 4.0 on 2022-01-07 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_price_remove_card_price_remove_card_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lotCategory', to='auctions.category')),
                ('lot_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lotname', to='auctions.card')),
                ('lot_price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lotPrice', to='auctions.price')),
            ],
        ),
    ]