# Generated by Django 3.2.6 on 2021-09-08 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SLB_App', '0004_recipe_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='steps',
        ),
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='C:/Users/luke_stevenson795/Documents/personal projects/Shopping_List_Builder/SLB_App/static/apple.jpg', upload_to=''),
        ),
    ]
