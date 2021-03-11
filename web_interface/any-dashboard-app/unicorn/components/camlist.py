from django_unicorn.components import UnicornView
from camsecuro.models import Cameras
from camsecuro.models import Addresses


class CamlistView(UnicornView):
    page_id = 1
    cameras = []
    address = ''

    playerLicence = "PLAY2-jPNR8-J8WTA-Eabzm-4Cj6E-u7CPZ"
    camerasHost = "https://mfc-video.site"

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)  # calling super is required
        print(kwargs.get("id"))
        self.page_id = kwargs.get("id")
        self.cameras = Cameras.objects.filter(address_id__id = self.page_id)
        print (self.cameras)
        self.address = Addresses.objects.get(id = self.page_id)