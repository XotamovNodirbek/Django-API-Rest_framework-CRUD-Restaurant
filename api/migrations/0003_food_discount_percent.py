# Generated by Django 5.1.4 on 2024-12-31 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_food_discount_percent_food_discounted_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='discount_percent',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
