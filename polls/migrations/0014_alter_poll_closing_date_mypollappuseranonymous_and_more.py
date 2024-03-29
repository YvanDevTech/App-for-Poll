# Generated by Django 4.1.2 on 2023-12-23 14:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0013_alter_poll_closing_date_delete_voter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='closing_date',
            field=models.DateField(default=datetime.date(2026, 9, 18), verbose_name='closing date * '),
        ),
        migrations.CreateModel(
            name='MyPollAppUserAnonymous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('certificate', models.CharField(max_length=255)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MyCandidatePreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_name', models.CharField(max_length=255)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.mypollappuseranonymous')),
            ],
        ),
    ]
