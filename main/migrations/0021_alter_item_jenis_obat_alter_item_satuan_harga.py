# Generated by Django 4.2.5 on 2023-09-19 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_item_expired_alter_item_jenis_obat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='jenis_obat',
            field=models.CharField(choices=[('Alergi', 'Alergi'), ('Penyakit Dalam', 'Penyakit dalam'), ('Herbal/Suplemen', 'Herbal/Suplemen'), ('Lansia', 'Penyakit Orang Tua'), ('Racik', 'Racik'), ('Anak (0-17 tahun)', 'Khusus Anak (0-17 tahun)'), ('Ibadah', 'Obat Hati'), ('Generic', 'Generic')], default='Generic', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='satuan_harga',
            field=models.CharField(choices=[('Botol', 'Botol/Sirup'), ('Sachete', 'Sachete'), ('Kotak/Kemasan', 'Kotak/Kemasan'), ('Strip', '1 Strip'), ('Kapsul', '1 Butir Kapsul')], default='Kapsul', max_length=100),
        ),
    ]
