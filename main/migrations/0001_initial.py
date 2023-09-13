# Generated by Django 4.2.5 on 2023-09-11 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('price', models.IntegerField()),
                ('jenis_obat', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('expired', models.DateField(auto_now=True)),
            ],
        ),
    ]
