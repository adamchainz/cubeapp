# Generated by Django 2.1.2 on 2018-10-14 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cubeapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abbreviation',
            name='real_objects',
        ),
        migrations.AddField(
            model_name='realobject',
            name='abbreviation',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cubeapp.Abbreviation'),
            preserve_default=False,
        ),
    ]