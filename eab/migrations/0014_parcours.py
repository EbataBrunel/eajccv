# Generated by Django 4.1.6 on 2023-03-08 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eab', '0013_matiere'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parcours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statut', models.CharField(choices=[('etudiant', 'Etudiant'), ('travailleur', 'Travailleur')], max_length=200, null=True)),
                ('niveau', models.CharField(choices=[('Bac + 1', 'Bac + 1'), ('Bac + 2', 'Bac + 2'), ('Bac + 3', 'Bac + 3'), ('Bac + 4', 'Bac + 4'), ('Bac + 5', 'Bac + 5'), ('Bac + 6', 'Bac + 6'), ('Bac + 7', 'Bac + 7')], max_length=200, null=True)),
                ('composant', models.CharField(max_length=100, null=True)),
                ('sous_composant', models.CharField(max_length=100, null=True)),
                ('annee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eab.annee')),
                ('etablissement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eab.etablissement')),
                ('formation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eab.formation')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eab.matiere')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]