# Generated by Django 2.2 on 2019-04-28 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='Cart_id',
            new_name='cart_id',
        ),
    ]
