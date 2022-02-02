# Generated by Django 4.0 on 2022-01-10 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_card_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='tag',
        ),
        migrations.AddField(
            model_name='lot',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='auctions.Lot'),
        ),
    ]