# Generated by Django 3.0.8 on 2020-08-24 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20200823_2133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='street_address1',
            new_name='street_address_1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='street_address2',
            new_name='street_address_2',
        ),
    ]
