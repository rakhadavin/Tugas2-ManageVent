# Generated by Django 4.2.5 on 2023-11-21 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_remove_item_gambar_alter_item_jenis_obat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='jenis_obat',
            field=models.CharField(choices=[('Generic', 'Generic'), ('Lansia', 'Penyakit Orang Tua'), ('Alergi', 'Alergi'), ('Anak (0-17 tahun)', 'Khusus Anak (0-17 tahun)'), ('Herbal/Suplemen', 'Herbal/Suplemen'), ('Penyakit Dalam', 'Penyakit dalam'), ('Ibadah', 'Obat Hati'), ('Racik', 'Racik')], default='Generic', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='satuan_harga',
            field=models.CharField(choices=[('Kapsul', '1 Butir Kapsul'), ('Kotak/Kemasan', 'Kotak/Kemasan'), ('Botol', 'Botol/Sirup'), ('Sachete', 'Sachete'), ('Strip', '1 Strip')], default='Kapsul', max_length=100),
        ),
    ]