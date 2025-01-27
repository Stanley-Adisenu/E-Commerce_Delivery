# Generated by Django 5.0.3 on 2024-07-17 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField()),
                ('delivery_status', models.CharField(choices=[('on_hold', 'on_hold'), ('ready', 'ready'), ('on_the_way', 'on_the_way'), ('delivered', 'delivered'), ('cancelled', 'cancelled')], max_length=50)),
                ('tracking_number', models.CharField(max_length=50)),
                ('courier', models.CharField(max_length=500)),
                ('estimated_delivery_date', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
