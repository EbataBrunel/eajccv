# Generated by Django 4.1.6 on 2023-03-11 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eab', '0026_matiere_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='competence',
            name='status',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='status',
            field=models.IntegerField(null=True),
        ),
    ]
