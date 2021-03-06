# Generated by Django 3.1.7 on 2021-03-21 12:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(verbose_name='age')),
                ('gender', models.CharField(max_length=10, verbose_name='gender')),
                ('game_type', models.CharField(max_length=100, verbose_name='type')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_tickets', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(4)], verbose_name='num_tickets')),
                ('competition', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='compPage.competition')),
            ],
        ),
    ]
