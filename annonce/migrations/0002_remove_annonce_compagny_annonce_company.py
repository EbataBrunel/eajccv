# Generated by Django 4.1.6 on 2023-05-19 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annonce', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annonce',
            name='compagny',
        ),
        migrations.AddField(
            model_name='annonce',
            name='company',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
