# Generated by Django 3.2.3 on 2021-05-28 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0003_auto_20210528_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionitem',
            name='acution_end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='auctionitem',
            name='auction_start_time',
            field=models.DateTimeField(null=True),
        ),
    ]
