# Generated by Django 2.1.4 on 2018-12-17 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0006_auto_20181217_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accident',
            name='status',
            field=models.CharField(choices=[('Expired', 'expired'), ('Pending', 'pending'), ('New', 'new'), ('Accepted', 'accepted')], default='Pending', max_length=120),
        ),
    ]