# Generated by Django 2.1.4 on 2018-12-16 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0002_accident_accident_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accident',
            name='accident_image',
        ),
        migrations.AlterField(
            model_name='accident',
            name='status',
            field=models.CharField(choices=[('Pending', 'pending'), ('Accepted', 'accepted'), ('Expired', 'expired')], default='Pending', max_length=120),
        ),
    ]
