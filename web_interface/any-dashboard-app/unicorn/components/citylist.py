from django_unicorn.components import UnicornView
from camsecuro.models import Addresses
from itertools import groupby
from django.db.models import Q
import re

class CitylistView(UnicornView):
    state = ''
    
    def addresses(self):
        if (self.state):
            # search = re.sub(r'[^A-Za-z]', '', self.state)
            # print(search)
            search = re.sub(r'[^а-яА-ЯёЁ]', '', self.state)
            print(search)
            return Addresses.objects.filter(
                Q(address__contains = search[1:]) |
                Q(city_id__city_name__contains = search[1:])
            )
        test = Addresses.objects.all()
        print(test[0].city_id.city_name)
        return Addresses.objects.all()