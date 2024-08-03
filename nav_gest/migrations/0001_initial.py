# Generated by Django 5.0.6 on 2024-08-01 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assigner_Voiture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ass', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_passager', models.IntegerField(default=0)),
                ('carburant', models.FloatField(default=0.0)),
                ('date_depart', models.DateTimeField(auto_now_add=True)),
                ('date_arrive', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Embarquation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('heure', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_etudiant', models.CharField(max_length=90, unique=True)),
                ('lieu_naissance', models.CharField(max_length=30)),
                ('date_naissance', models.CharField(max_length=10)),
                ('matricule', models.CharField(max_length=10)),
                ('promotion', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Moyen_Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='photo_profile')),
                ('nom_mt', models.CharField(blank=True, max_length=70, unique=True)),
                ('capacite', models.IntegerField()),
                ('type_voiture', models.CharField(choices=[('bus', 'Bus'), ('coast', 'Coaster'), ('voi', 'Voiture Luxe')], max_length=5)),
            ],
        ),
    ]
