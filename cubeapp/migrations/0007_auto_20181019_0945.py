# Generated by Django 2.1.2 on 2018-10-19 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cubeapp', '0006_illegalletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abbreviation',
            name='second',
            field=models.CharField(blank=True, max_length=1),
        ),
    ]