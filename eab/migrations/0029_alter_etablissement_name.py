# Generated by Django 4.1.6 on 2023-03-11 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eab', '0028_remove_matiere_status_parcours_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etablissement',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
