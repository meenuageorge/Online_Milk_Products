# Generated by Django 4.1.2 on 2022-11-17 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cowapp', '0002_alter_post_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_vaccination', models.DateField()),
            ],
        ),
    ]