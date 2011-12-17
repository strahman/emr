#!/usr/bin/env python
from optparse import make_option
from django.core.management.commands.dumpdata import Command as Dumpdata
from django.conf import settings

from card.models import UserCard

import datetime


d = lambda x:  datetime.datetime.strptime(x, '%d.%m.%Y').date()  if x else None

class Command(Dumpdata):
    option_list = Dumpdata.option_list + (
        make_option('--pretty', default=False, action='store_true', 
            dest='pretty', help='Avoid unicode escape symbols'
        ),
    )
    
    def handle(self, *args, **kwargs):
        data = super(Command, self).handle(*args, **kwargs)
        f = open('apps/data.txt', 'r')



        model_fields = [i.name for i in UserCard._meta.fields]
        model_fields.remove('id')


        for item in f:
            l_st = item.split(',')
            m = zip(model_fields, l_st)
            print "OK"
            print m
            m = dict(m)
            birthday = d(m['birthday'])
            print birthday
            del m['birthday']
            m['city'] = None
            m['oblast'] = None
            m['birthday'] = birthday
            m['last_visit'] = None
            card = UserCard(**m)
            #card.birthday = birthday
            card.save()
        


