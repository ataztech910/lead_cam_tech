from django_unicorn.components import UnicornView
from camsecuro.models import Addresses
from itertools import groupby
from django.db.models import Q
import re
import operator

class CitylistView(UnicornView):
    state = ''
    
    def addresses(self):
        if (self.state):
            search = re.sub(r'[^а-яА-ЯёЁ]', '', self.state)
            print(search)
            return Addresses.objects.filter(
                Q(address__contains = search[1:]) |
                Q(city_id__city_name__contains = search[1:])
            )
        addresses = Addresses.objects.order_by('city_id__city_name').all()
        # self.serve_array(addresses)
        return addresses
        # return self.serve_array(addresses)

    def serve_array(self, addresses):
        reMap = []
        for item in addresses.iterator():
            # print(item.letter)
            data = [item, item.city_id.city_name[0]]
            reMap.append(data)
            # item.letter = item.city_id.city_name[0]
        print(reMap)
        return reMap