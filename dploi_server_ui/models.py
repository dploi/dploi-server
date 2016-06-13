#-*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from dploi_server.models import Realm


#class CustomerOrganisation(models.Model):
#    name = models.CharField(max_length=128)
#    realms = models.ManyToManyField(Realm) # Which realms can this customer deploy to?
#    users = models.ManyToManyField(User)