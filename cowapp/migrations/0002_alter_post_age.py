# Generated by Django 4.1.2 on 2022-11-17 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cowapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='age',
            field=models.TextField(),
        ),
    ]