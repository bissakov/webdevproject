# Generated by Django 2.2.20 on 2021-05-05 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_product_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='ammount',
            new_name='amount',
        ),
    ]
