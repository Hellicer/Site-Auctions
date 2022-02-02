# Generated by Django 4.0 on 2022-01-14 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0036_alter_card_status_lot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cardwatchlist', to='auctions.card')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Userwatchlist', to='auctions.user')),
            ],
        ),
    ]
