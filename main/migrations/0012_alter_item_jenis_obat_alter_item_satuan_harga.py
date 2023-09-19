# Generated by Django 4.2.5 on 2023-09-19 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_item_jenis_obat_alter_item_satuan_harga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='jenis_obat',
            field=models.CharField(choices=[('An', 'Khusus Anak (0-17 tahun)'), ('g', 'Generic'), ('ot', 'Penyakit Orang Tua'), ('r', 'Racik'), ('h', 'Herbal/Suplemen'), ('pd', 'Penyakit dalam'), ('a', 'Alergi')], default='Generic', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='satuan_harga',
            field=models.CharField(choices=[('c', '1 Butir Kapsul'), ('b', 'Botol/Sirup'), ('k', 'Kotak/Kemasan'), ('s', '1 Strip')], default='Kapsul', max_length=100),
        ),
    ]
