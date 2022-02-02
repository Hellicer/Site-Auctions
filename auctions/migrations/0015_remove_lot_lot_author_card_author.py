# Generated by Django 4.0 on 2022-01-09 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_remove_lot_lot_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lot',
            name='lot_author',
        ),
        migrations.AddField(
            model_name='card',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='lotAuthor', to='auctions.user'),
        ),
    ]
