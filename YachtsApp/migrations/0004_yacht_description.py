# Generated by Django 4.0 on 2022-01-03 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YachtsApp', '0003_yacht_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='yacht',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
