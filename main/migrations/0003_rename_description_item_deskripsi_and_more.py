# Generated by Django 4.2.5 on 2023-09-11 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_item_satuan_harga_alter_item_jenis_obat_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='description',
            new_name='deskripsi',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='price',
            new_name='harga',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='name',
            new_name='nama_obat',
        ),
        migrations.RemoveField(
            model_name='item',
            name='expired',
        ),
        migrations.AlterField(
            model_name='item',
            name='jenis_obat',
            field=models.CharField(choices=[('An', 'Khusus Anak (0-17 tahun)'), ('h', 'Herbal/Suplemen'), ('ot', 'Penyakit Orang Tua'), ('a', 'Alergi'), ('pd', 'Penyakit dalam'), ('g', 'Generic'), ('r', 'Racik')], default='Generic', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='satuan_harga',
            field=models.CharField(choices=[('s', '1 Strip'), ('c', '1 Butir Kapsul'), ('k', 'Kotak/Kemasan'), ('b', 'Botol/Sirup')], default='Kapsul', max_length=100),
        ),
    ]
