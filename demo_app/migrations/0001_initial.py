# Generated by Django 4.1.5 on 2023-01-03 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Racer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('skill', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=200)),
                ('car_power', models.IntegerField()),
                ('year', models.DateTimeField()),
                ('racer_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='demo_app.racer')),
            ],
        ),
    ]
