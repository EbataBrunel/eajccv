# Generated by Django 4.1.6 on 2023-03-08 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eab', '0012_entreprise'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=200)),
                ('abreviation', models.CharField(max_length=50)),
            ],
        ),
    ]
