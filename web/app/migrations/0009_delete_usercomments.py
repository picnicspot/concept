# Generated by Django 3.1 on 2020-09-06 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_usercomments'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserComments',
        ),
    ]