# Generated by Django 4.2.5 on 2023-10-12 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0022_alter_riwayat_pengguna_penyakit_genetik'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riwayat_pengguna',
            name='penyakit_genetik',
            field=models.CharField(choices=[('N', 'Tidak'), ('Y', 'Ya')], max_length=5),
        ),
    ]
