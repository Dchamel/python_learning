# Generated by Django 4.1.7 on 2023-03-24 15:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0002_products_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='short_description',
            field=models.TextField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
