# Generated by Django 2.1.2 on 2018-10-19 08:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cubeapp', '0005_auto_20181019_0920'),
    ]

    operations = [
        migrations.CreateModel(
            name='IllegalLetter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.CharField(max_length=1)),
                ('replace', models.CharField(max_length=1)),
                ('user', models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'IllegalLetter',
                'verbose_name_plural': 'IllegalLetters',
            },
        ),
    ]
