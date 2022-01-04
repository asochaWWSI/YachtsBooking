# Generated by Django 4.0 on 2022-01-04 17:57

from django.db import migrations

def insert_initial(apps, schema_editor):
    Yacht = apps.get_model('YachtsApp', 'Yacht')
    Customer = apps.get_model('YachtsApp', 'Customer')
    Booking = apps.get_model('YachtsApp', 'Booking')
    
    create_yacht = Yacht.objects.create
    yachts = [
        create_yacht(name='Nadzieja',type='śródlądowa',year_of_production='1998-01-01',engine_power='Spalinowy',length='3',width='2',mass_kg='600',price=1000.00,description='Bardzo ładna łódź'),
        create_yacht(name='Slonce',type='śródlądowa',year_of_production='2022-01-01',engine_power='Elektryczny',length='5',width='3',mass_kg='800',price=1200.00,description='Bardzo ładna łódź'),
        create_yacht(name='Ksiezyc',type='śródlądowa',year_of_production='1998-01-01',engine_power='Spalinowy',length='6',width='4',mass_kg='1000',price=1500.00,description='Bardzo ładna łódź'),
        create_yacht(name='OMEN',type='Morska',year_of_production='2005-01-01',engine_power='Spalinowy',length='6',width='5',mass_kg='1200',price=2100.00,description='Bardzo ładna łódź'),
        create_yacht(name='Chmurka',type='Morska',year_of_production='1998-01-01',engine_power='Elektryczny',length='8',width='6',mass_kg='1400',price=2600.00,description='Bardzo ładna łódź'),
        create_yacht(name='Orion',type='Morska',year_of_production='2010-01-01',engine_power='Elektryczny',length='12',width='7',mass_kg='1600',price=4000.00,description='Bardzo ładna łódź'),
    ]
    for y in yachts:
        y.save()
    
    create_custormer = Customer.objects.create
    customers = [
        create_custormer(name='Zbyszek',surname='Zbojnik',telephone='+48 533 521 523',email='Zbyszek54@gmail.com'),
        create_custormer(name='Anna',surname='Wiraszka',telephone='+48 224 432 534',email='Annatoja@onet.pl'),
        create_custormer(name='Pawel',surname='Gawel',telephone='+48 453 654 432',email='Gawel@wp.pl'),
    ]
    for c in customers:
        c.save()
 
    create_bookin = Booking.objects.create
    b = create_bookin(date_lend='2021-06-07',date_return='2021-06-09',final_price=3000.00,customer=customers[0],yachts=yachts[0])
    b.save()


class Migration(migrations.Migration):

    dependencies = [
        ('YachtsApp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_initial)
    ]
