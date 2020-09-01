# Generated by Django 3.1 on 2020-08-31 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mapbox_location_field.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('website', models.URLField(null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bench',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, null=True)),
                ('description', models.CharField(blank=True, max_length=350, null=True)),
                ('location', mapbox_location_field.models.LocationField(map_attrs={})),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.CharField(choices=[('Picnic Bench', 'Picnic Bench'), ('Park Bench', 'Park Bench'), ('Picnicspot', 'Picnicspot'), ('Picnic Area', 'Picnic Area')], max_length=30, null=True)),
                ('condition', models.CharField(choices=[('Spanking', 'Spanking'), ('Okay', 'Okay'), ('Apalling', 'Appalling'), ('Not There', 'Not There')], max_length=30, null=True)),
                ('capacity', models.CharField(choices=[('1-2', '1-2'), ('3-5', '3-5'), ('6-10', '6-10'), ('10+', '10+')], max_length=30, null=True)),
                ('tag', models.ManyToManyField(to='app.Tag')),
            ],
        ),
    ]
