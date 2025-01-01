# Generated by Django 5.1.4 on 2024-12-31 13:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category'),
        ),
        migrations.AlterField(
            model_name='food',
            name='discount_percent',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='food',
            name='photo',
            field=models.ImageField(default=1, upload_to='media/food/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]