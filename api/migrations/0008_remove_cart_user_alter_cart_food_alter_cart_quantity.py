# Generated by Django 5.1.4 on 2025-01-01 01:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_food_category_alter_food_discount_percent_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.AlterField(
            model_name='cart',
            name='food',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.food'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
