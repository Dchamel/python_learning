# Generated by Django 4.1.7 on 2023-03-14 13:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('landing', '0002_rename_subscribers_subscriber'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscriber',
            new_name='Subscribers',
        ),
        migrations.AlterModelOptions(
            name='subscribers',
            options={'verbose_name': 'Subscribers', 'verbose_name_plural': 'Subscribers'},
        ),
    ]
