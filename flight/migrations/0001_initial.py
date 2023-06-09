# Generated by Django 4.1.7 on 2023-02-19 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirlineCompanies',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20, unique=True)),
                ('credit_card_number', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('departure_time', models.DateTimeField()),
                ('landing_time', models.DateTimeField()),
                ('remaining_tickets', models.IntegerField(default=0)),
                ('airline_company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.airlinecompanies')),
                ('destination_country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_country_id', to='flight.countries')),
                ('origin_country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin_country_id', to='flight.countries')),
            ],
        ),
        migrations.CreateModel(
            name='UserRoles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=40, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.userroles')),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.customers')),
                ('flight_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.flights')),
            ],
        ),
        migrations.AddField(
            model_name='customers',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.users'),
        ),
        migrations.AddField(
            model_name='airlinecompanies',
            name='country_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.countries'),
        ),
        migrations.AddField(
            model_name='airlinecompanies',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.users'),
        ),
        migrations.CreateModel(
            name='Adminstrators',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.users')),
            ],
        ),
    ]
