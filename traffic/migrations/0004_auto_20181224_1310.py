# Generated by Django 2.1.4 on 2018-12-24 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0003_auto_20181224_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Involved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Declined', 'Declined'), ('No Response', 'No Response'), ('Accepted', 'Accepted')], default='No response', max_length=120)),
            ],
        ),
        migrations.RenameField(
            model_name='accident',
            old_name='involved',
            new_name='involved_people',
        ),
        migrations.AlterField(
            model_name='accident',
            name='status',
            field=models.CharField(choices=[('Expired', 'expired'), ('Accepted', 'accepted'), ('New', 'new'), ('Pending', 'pending')], default='New', max_length=120),
        ),
        migrations.AddField(
            model_name='involved',
            name='accident',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traffic.Accident'),
        ),
        migrations.AddField(
            model_name='involved',
            name='involved',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traffic.Profile'),
        ),
    ]
