# Generated by Django 4.2.5 on 2023-09-19 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_alter_riwayat_pengguna_penyakit_genetik'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riwayat_pengguna',
            name='penyakit_genetik',
            field=models.CharField(choices=[('Y', 'Ya'), ('N', 'Tidak')], max_length=5),
        ),
    ]
