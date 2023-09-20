# Generated by Django 4.2.5 on 2023-09-19 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_item_expired_alter_item_jenis_obat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='jenis_obat',
            field=models.CharField(choices=[('An', 'Khusus Anak (0-17 tahun)'), ('a', 'Alergi'), ('g', 'Generic'), ('ot', 'Penyakit Orang Tua'), ('r', 'Racik'), ('h', 'Herbal/Suplemen'), ('pd', 'Penyakit dalam')], default='Generic', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='satuan_harga',
            field=models.CharField(choices=[('s', '1 Strip'), ('c', '1 Butir Kapsul'), ('b', 'Botol/Sirup'), ('k', 'Kotak/Kemasan')], default='Kapsul', max_length=100),
        ),
    ]