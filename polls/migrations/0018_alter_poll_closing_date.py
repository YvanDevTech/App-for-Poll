# Generated by Django 4.1.2 on 2024-01-23 07:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_alter_poll_closing_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='closing_date',
            field=models.DateField(default=datetime.date(2026, 10, 19), verbose_name='closing date * '),
        ),
    ]
