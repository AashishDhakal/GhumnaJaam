# Generated by Django 3.0.2 on 2020-01-23 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hirings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('hiringdetail', models.TextField(default='I want to hire you on this day.')),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.GuideProfile')),
                ('tourist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.TouristProfile')),
            ],
            options={
                'verbose_name_plural': 'Hirings',
            },
        ),
    ]
