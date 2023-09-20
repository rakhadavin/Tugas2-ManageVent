# Generated by Django 4.2.5 on 2023-09-19 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_item_expired_alter_item_jenis_obat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='expired',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='jenis_obat',
            field=models.CharField(choices=[('Generic', 'Generic'), ('Alergi', 'Alergi'), ('Herbal/Suplemen', 'Herbal/Suplemen'), ('Lansia', 'Penyakit Orang Tua'), ('Obat Hati', 'Ibadah'), ('Penyakit Dalam', 'Penyakit dalam'), ('Anak (0-17 tahun)', 'Khusus Anak (0-17 tahun)'), ('Racik', 'Racik')], default='Generic', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='satuan_harga',
            field=models.CharField(choices=[('Strip', '1 Strip'), ('Sachete', 'Sachete'), ('Kotak/Kemasan', 'Kotak/Kemasan'), ('Botol', 'Botol/Sirup'), ('Kapsul', '1 Butir Kapsul')], default='Kapsul', max_length=100),
        ),
    ]