# Generated by Django 4.1.2 on 2024-01-25 09:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_alter_poll_closing_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='closing_date',
            field=models.DateField(default=datetime.date(2026, 10, 21), verbose_name='closing date * '),
        ),
        migrations.AlterField(
            model_name='votingpoll',
            name='preference_model',
            field=models.CharField(choices=[('Ranks#3', 'Approval Voting (Yes / No)'), ('Ranks#0', 'Simpson voting'), ('Ranks#2', 'Borda voting'), ('Ranks#4', 'Copeland voting'), ('Ranks#6', 'schulze voting'), ('Ranks#8', 'Hare voting')], default='PositiveNegative', max_length=50, verbose_name='Preference model * '),
        ),
    ]