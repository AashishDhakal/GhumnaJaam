# Generated by Django 3.0.2 on 2020-01-24 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guideprofile',
            name='earning',
            field=models.IntegerField(default=0),
        ),
    ]
