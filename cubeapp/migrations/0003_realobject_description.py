# Generated by Django 2.1.2 on 2018-10-15 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cubeapp', '0002_auto_20181014_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='realobject',
            name='description',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]