# Generated by Django 4.0 on 2022-01-03 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40, null=True)),
                ('surname', models.CharField(max_length=40, null=True)),
                ('telephone', models.CharField(max_length=15, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Yacht',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name_yacht', models.CharField(max_length=50)),
                ('type_yaht', models.CharField(max_length=50)),
                ('year_of_production', models.DateField()),
                ('engine_power', models.CharField(max_length=50)),
                ('length', models.IntegerField()),
                ('width', models.IntegerField()),
                ('mass_kg', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date_lend', models.DateField()),
                ('date_return', models.DateField()),
                ('id_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YahtsApp.customer')),
                ('id_yachts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YahtsApp.yacht')),
            ],
        ),
    ]