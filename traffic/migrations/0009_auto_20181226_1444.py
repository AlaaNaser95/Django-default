# Generated by Django 2.1.4 on 2018-12-26 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0008_auto_20181225_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accident',
            name='status',
            field=models.CharField(choices=[('Accepted', 'accepted'), ('Pending', 'pending'), ('New', 'new'), ('Expired', 'expired')], default='New', max_length=120),
        ),
        migrations.AlterField(
            model_name='involved',
            name='status',
            field=models.CharField(choices=[('No Response', 'No Response'), ('Declined', 'Declined'), ('Accepted', 'Accepted')], default='No response', max_length=120),
        ),
    ]
