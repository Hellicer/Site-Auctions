# Generated by Django 4.0 on 2022-01-12 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0028_alter_card_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='lotAuthor', to='auctions.user'),
        ),
    ]
