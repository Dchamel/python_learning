# Generated by Django 4.2.5 on 2023-09-29 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='images/default.png', upload_to='images/'),
        ),
    ]