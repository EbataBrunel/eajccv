# Generated by Django 4.1.6 on 2023-03-04 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eab', '0002_annee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annee',
            name='libelle',
            field=models.CharField(max_length=4, null=True, unique=True),
        ),
    ]
