# Generated by Django 4.1.6 on 2023-04-06 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eab', '0043_alter_profile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcours',
            name='annee1',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='apropos',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='droitmes',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Masculin', 'Masculin'), ('Feminin', 'Feminin')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='priority',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profession',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='vaform',
            field=models.CharField(choices=[('Visible', 'Visible'), ('Invisible', 'Invisible')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='vcomp',
            field=models.CharField(choices=[('Visible', 'Visible'), ('Invisible', 'Invisible')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='vep',
            field=models.CharField(choices=[('Visible', 'Visible'), ('Invisible', 'Invisible')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='vform',
            field=models.CharField(choices=[('Visible', 'Visible'), ('Invisible', 'Invisible')], default='Visible', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='datecontact',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='date_debut',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='date_fin',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='parametre',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='parcours',
            name='annee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eab.annee'),
        ),
    ]