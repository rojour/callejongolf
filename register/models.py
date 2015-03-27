from django.db import models
from django.utils import timezone

class Player(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)
    shirt = models.CharField(max_length=4)
    email = models.EmailField(max_length=75, default='')
    phone = models.CharField(max_length =12, default='')
    comments = models.TextField(default='', null=True, blank=True)
    group_play = models.CharField(max_length=2, null=True, blank=True)
    pay_method = models.CharField(max_length=15, null=True, blank=True)
    pay_status = models.CharField(max_length=10, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    
    def publish(self):
        self.created_date = timezone.now()

    def __str__(self):
        return self.last_name + ', ' + self.first_name
