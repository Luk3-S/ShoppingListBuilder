# Generated by Django 3.2.6 on 2021-09-21 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SLB_App', '0014_auto_20210921_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='basketNum',
            field=models.IntegerField(default=9999999),
        ),
    ]