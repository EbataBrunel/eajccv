# Generated by Django 4.1.6 on 2023-03-21 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eab', '0041_alter_parametre_appeditor_alter_parametre_devise_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parametre',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]