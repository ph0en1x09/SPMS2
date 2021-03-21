# Generated by Django 3.1.7 on 2021-03-21 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('text', models.CharField(max_length=500, verbose_name='text')),
                ('reply', models.CharField(default='Thanks for your feedback', max_length=500, verbose_name='reply')),
                ('is_read', models.BooleanField(default=False)),
                ('member', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mysite.member')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('feedback_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='suggestionPortal.feedback')),
                ('coordinator', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mysite.coordinator')),
            ],
            bases=('suggestionPortal.feedback',),
        ),
    ]
