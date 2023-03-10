# Generated by Django 4.1.2 on 2022-11-22 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cowapp', '0005_neweartag'),
    ]

    operations = [
        migrations.CreateModel(
            name='MilkRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('userid', models.TextField()),
                ('address', models.TextField()),
                ('date', models.DateField()),
                ('morning_milk_record', models.TextField()),
                ('evening_milk_record', models.TextField()),
                ('payment', models.TextField()),
            ],
        ),
    ]
