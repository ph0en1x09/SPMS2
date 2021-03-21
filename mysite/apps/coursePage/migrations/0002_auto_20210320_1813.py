# Generated by Django 3.1.2 on 2021-03-20 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mysite', '0003_auto_20210320_1813'),
        ('coursePage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='in_coordinator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.coordinator'),
        ),
        migrations.AddField(
            model_name='course',
            name='in_slots',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mysite.slot'),
        ),
        migrations.AddField(
            model_name='course',
            name='in_students',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mysite.member'),
        ),
    ]
