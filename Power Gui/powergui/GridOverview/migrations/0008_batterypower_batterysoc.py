# Generated by Django 4.1.7 on 2023-04-02 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GridOverview', '0007_totaldiesel_totalsolar_totalwind'),
    ]

    operations = [
        migrations.CreateModel(
            name='batteryPower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='batterySOC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soc', models.JSONField()),
            ],
        ),
    ]
