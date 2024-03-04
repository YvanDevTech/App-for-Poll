# Generated by Django 4.1.2 on 2023-11-25 21:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_delete_polldata_delete_voter_alter_poll_closing_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('participation_link', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='poll',
            name='closing_date',
            field=models.DateField(default=datetime.date(2026, 8, 21), verbose_name='closing date * '),
        ),
    ]