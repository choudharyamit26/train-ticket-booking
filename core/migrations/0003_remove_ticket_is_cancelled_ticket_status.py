# Generated by Django 4.2 on 2023-06-17 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_booking_ticket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='is_cancelled',
        ),
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.CharField(default='Waiting', max_length=100),
        ),
    ]