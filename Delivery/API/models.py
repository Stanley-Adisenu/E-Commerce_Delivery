from django.db import models

# Create your models here.

class Delivery(models.Model):
    STATUS_CHOICES = (
    ('on_hold', 'on_hold'),
    ('ready', 'ready'),
    ('on_the_way', 'on_the_way'),
    ('delivered', 'delivered'),
    ('cancelled', 'cancelled'),
    )


    order_id = models.IntegerField()
    delivery_status = models.CharField(choices=STATUS_CHOICES, max_length=50)
    tracking_number = models.CharField( max_length=50)
    courier = models.CharField( max_length=500)
    estimated_delivery_date = models.DateTimeField( auto_now_add=True)
    created_at =  models.DateTimeField( auto_now=True)
    updated_at =  models.DateTimeField( auto_now=True)
