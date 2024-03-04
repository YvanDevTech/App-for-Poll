# Generated by Django 4.1.2 on 2023-11-24 16:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_remove_polldata_column2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PollData',
        ),
        migrations.DeleteModel(
            name='Voter',
        ),
        migrations.AlterField(
            model_name='poll',
            name='closing_date',
            field=models.DateField(default=datetime.date(2026, 8, 20), verbose_name='closing date * '),
        ),
    ]