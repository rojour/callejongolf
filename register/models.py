from django.db import models
from django.utils import timezone

class Sponsor(models.Model):
    cont_first_name = models.CharField(max_length=20)
    cont_last_name = models.CharField(max_length=20)
    cont_email = models.EmailField(max_length=75, default='')
    cont_phone = models.CharField(max_length=12, default='')
    cont_comments = models.TextField(default='', null=True, blank=True)
    sponsor_name = models.CharField(max_length=30)
    sponsor_type = models.CharField(max_length=10)
    sponsor_pay_status = models.CharField(max_length=10, null=True, blank=True)
    sponsor_pay_method = models.CharField(max_length=15, null=True, blank=True)
    sponsor_created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.sponsor_created_date = timezone.now()

    def __unicode__(self):
        return self.sponsor_name



class Player(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    shirt = models.CharField(max_length=4)
    gender = models.CharField(max_length=1, default='')
    email = models.EmailField(max_length=75, default='')
    phone = models.CharField(max_length =12, default='')
    comments = models.TextField(default='', null=True, blank=True)
    group_play = models.CharField(max_length=2, null=True, blank=True)
    pay_method = models.CharField(max_length=15, null=True, blank=True)
    pay_status = models.CharField(max_length=10, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    sponsor = models.ForeignKey(Sponsor, null=True, blank=True)
    
    def publish(self):
        self.created_date = timezone.now()

    def __unicode__(self):
        return self.last_name + ', ' + self.first_name

