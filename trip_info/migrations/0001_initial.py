# Generated by Django 4.1 on 2022-09-04 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityArrive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_arr', models.CharField(max_length=100, verbose_name='Arrivals')),
            ],
        ),
        migrations.CreateModel(
            name='CityDeparte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_dep', models.CharField(max_length=100, verbose_name='Departures')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='Departures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight', models.CharField(max_length=100, verbose_name='Flight')),
                ('plane', models.CharField(max_length=100, verbose_name='Plane')),
                ('schedule_dep', models.CharField(max_length=50, verbose_name='Schedule Departure')),
                ('schedule_arr', models.CharField(max_length=50, verbose_name='Schedule Arrivals')),
                ('city_arrive', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='trip_info.cityarrive')),
                ('city_departure', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='trip_info.citydeparte')),
                ('status', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='trip_info.status')),
            ],
        ),
    ]
