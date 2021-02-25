from django_unicorn.components import UnicornView
from django.conf import settings


class LeftmenuView(UnicornView):
    menu = [{'id': 'cameras', 'value': 'Камеры'},
            {'id': 'exit', 'value': 'Выход'}, ]
    static = settings.STATIC_URL
    pass
