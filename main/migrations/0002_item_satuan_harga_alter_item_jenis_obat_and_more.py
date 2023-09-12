# Generated by Django 4.2.5 on 2023-09-11 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='satuan_harga',
            field=models.CharField(choices=[('k', 'Kotak/Kemasan'), ('c', '1 Butir Kapsul'), ('b', 'Botol/Sirup'), ('s', '1 Strip')], default='Kapsul', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='jenis_obat',
            field=models.CharField(choices=[('r', 'Racik'), ('h', 'Herbal/Suplemen'), ('An', 'Khusus Anak (0-17 tahun)'), ('a', 'Alergi'), ('g', 'Generic'), ('pd', 'Penyakit dalam'), ('ot', 'Penyakit Orang Tua')], default='Generic', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]
