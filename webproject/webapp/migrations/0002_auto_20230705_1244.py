# Generated by Django 3.2.12 on 2023-07-05 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartItem',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
