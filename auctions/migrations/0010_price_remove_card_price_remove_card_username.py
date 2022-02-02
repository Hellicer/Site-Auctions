# Generated by Django 4.0 on 2022-01-07 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_card_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0, max_length=32)),
            ],
        ),
        migrations.RemoveField(
            model_name='card',
            name='price',
        ),
        migrations.RemoveField(
            model_name='card',
            name='username',
        ),
    ]