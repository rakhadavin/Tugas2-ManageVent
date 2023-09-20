# Generated by Django 4.2.5 on 2023-09-17 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data_pengguna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_pengguna', models.CharField(max_length=50)),
                ('email_pengguna', models.EmailField(max_length=254)),
                ('pass_pengguna', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='riwayat_pengguna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('penyakit', models.CharField(max_length=500)),
                ('usia', models.PositiveIntegerField(verbose_name='Usia')),
                ('penyakit_genetik', models.CharField(choices=[('N', 'Tidak'), ('Y', 'Ya')], max_length=5)),
            ],
        ),
    ]