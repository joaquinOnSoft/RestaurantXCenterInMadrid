import json
import re

from joaquinonsoft.net.HTTPRequest import HTTPRequest


class RodillasLocatorURLReader(HTTPRequest):
    URL_BASE = "https://www.rodilla.es/restaurantes"

    def __init__(self):
        super().__init__(self.URL_BASE, self.METHOD_GET)

    def read(self):
        response = super().read()

        locations = []

        lat = re.findall(r"data-lat=\"(.*)\"", response)
        lng = re.findall(r"data-lng=\"(.*)\"", response)
        name = re.findall(r"<h3 class=\"h3\">(.*)<", response)
        address = re.findall(r"<p class=\"search-restaurant-address\">(.*)<", response)
        phone = re.findall(r"<p class=\"search-restaurant-phone\">(.*)<", response)

        print("lats: ", len(lat))
        print("lngs: ", len(lng))
        print("h3: ", len(name))
        print("address: ", len(address))
        print("phone: ", len(phone))

        for i in range(len(lat)):
            location = {"latitude": lat[i],
                        "longitude": lng[i],
                        "name": name[i],
                        "address": address[i],
                        "phone": phone[i]}

            locations.append(location)

            print(lat[i], lng[i], name[i], address[i], phone[i])

        return response
