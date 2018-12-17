# Generated by Django 2.1.4 on 2018-12-17 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0010_auto_20181217_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accident',
            name='status',
            field=models.CharField(choices=[('Accepted', 'accepted'), ('Pending', 'pending'), ('New', 'new'), ('Expired', 'expired')], default='New', max_length=120),
        ),
    ]