# Generated by Django 4.0 on 2022-01-16 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0043_remove_watchlist_title_watchlist_watch'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='lot',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='CardWatchlist', to='auctions.card'),
            preserve_default=False,
        ),
    ]
