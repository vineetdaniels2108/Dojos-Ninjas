# Generated by Django 3.1.7 on 2021-03-06 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojos_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='Old Dojo', max_length=240),
        ),
    ]
