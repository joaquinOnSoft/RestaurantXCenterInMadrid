import json
import re

from joaquinonsoft.net.HTTPRequest import HTTPRequest


class VIPsLocatorURLReader(HTTPRequest):
    URL_BASE = "https://www.vips.es/localizador"

    PARAM_ADDRESS = "address"
    PARAM_LAT = "lat"
    PARAM_LNG = "lng"
    PARAM_DISTANCE = "distance"
    PARAM_CITIES = "cities"
    PARAM_OPTIONS_0 = "option_vips[0]"
    PARAM_OPTIONS_1 = "option_vips[1]"

    # 00 = '<div class="field field-name-field-store-name field-type-text field-label-hidden"><div class="field-items"><div class="field-item even">VIPS Sol</div></div></div>'
    # 01 = '40.416727'
    # 02 = '-3.703387'
    # 03 = '<div class="field field-name-field-store-phone field-type-text field-label-hidden"><div class="field-items"><div class="field-item even">669148462</div></div></div>'
    # 04 = ''
    # 05 = 'Puerta del Sol, 3'
    # 06 = 'Madrid'
    # 07 = '<div class="field field-name-field-store-transport field-type-text-long field-label-hidden"><div class="field-items"><div class="field-item even">Tren: C3 y C4 cercanias. Metro: Lineas 1,2,3</div></div></div>'
    # 08 = '3'
    # 09 = '74449'
    # 10 = 'VIPS Sol'
    STEP_NAME_HTML = 0
    STEP_LATITUDE = 1
    STEP_LONGITUDE = 2
    STEP_PHONE = 3
    STEP_ADDRESS_1 = 4
    STEP_ADDRESS_2 = 5
    STEP_ADDRESS_3 = 6
    STEP_TRANSPORT = 7
    STEP_NUMBER = 8
    STEP_ID = 9
    STEP_NAME = 10

    def __init__(self, address="Madrid, España", lat="40.4167754", lng="-3.7037902", distance="100", cities="none"):
        super().__init__(self.URL_BASE, self.METHOD_POST)
        self.params = {
            self.PARAM_ADDRESS: address,
            self.PARAM_LAT: lat,
            self.PARAM_LNG: lng,
            self.PARAM_DISTANCE: distance,
            self.PARAM_CITIES: cities,
            self.PARAM_OPTIONS_0: "4",
            self.PARAM_OPTIONS_1: "3"
        }

    def read(self):
        response = super().read()

        jsonObj = json.loads(response)

        locations = []
        for location in jsonObj['locations']:
            loc = {}
            address = ''
            for i in range(len(location)):
                if i == self.STEP_LATITUDE:
                    loc['latitude'] = location[i]
                elif i == self.STEP_LONGITUDE:
                    loc['longitude'] = location[i]
                elif i == self.STEP_PHONE:
                    phone = re.sub(r"<[^>]*>", "", location[i])
                    if phone is not None:
                        loc['phone'] = phone
                elif i == self.STEP_ADDRESS_1 and location[i] is not None and location[i] != '':
                    address += location[i] + " "
                elif i == self.STEP_ADDRESS_2:
                    address += location[i]
                elif i == self.STEP_ADDRESS_3:
                    loc['address'] = address + " " + location[i]
                elif i == self.STEP_NAME:
                    loc['name'] = location[i]

            locations.append(loc)

        return locations
