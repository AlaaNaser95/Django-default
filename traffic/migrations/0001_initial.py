
# Generated by Django 2.1.4 on 2018-12-21 12:02


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import traffic.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_longitude', models.DecimalField(decimal_places=6, default=1, max_digits=9)),
                ('location_latitude', models.DecimalField(decimal_places=6, default=1, max_digits=9)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'pending'), ('Expired', 'expired'), ('Accepted', 'accepted')], default='Pending', max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accident_image', models.FileField(upload_to='', validators=[traffic.validators.validate_file_extension])),
                ('accident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traffic.Accident')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('civil_id', models.CharField(max_length=120)),
                ('phone_no', models.CharField(blank=True, max_length=120, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regist_image', models.ImageField(upload_to='')),
                ('accident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traffic.Accident')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examiner', models.CharField(max_length=120)),
                ('comment', models.TextField()),
                ('reported_at', models.DateTimeField(auto_now_add=True)),
                ('accident', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='traffic.Accident')),
                ('detective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='accident',
            name='involved',
            field=models.ManyToManyField(to='traffic.Profile'),
        ),
    ]
