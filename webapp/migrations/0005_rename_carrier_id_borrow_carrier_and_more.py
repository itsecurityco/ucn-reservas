# Generated by Django 4.0.3 on 2022-03-20 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_borrow_carrier_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrow',
            old_name='carrier_id',
            new_name='carrier',
        ),
        migrations.RenameField(
            model_name='borrow',
            old_name='device_id',
            new_name='device',
        ),
        migrations.RenameField(
            model_name='borrow',
            old_name='user_id',
            new_name='user',
        ),
    ]
