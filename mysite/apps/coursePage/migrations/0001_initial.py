# Generated by Django 3.1.2 on 2021-03-20 18:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='name')),
                ('num_students', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(50)], verbose_name='num_students')),
            ],
        ),
    ]