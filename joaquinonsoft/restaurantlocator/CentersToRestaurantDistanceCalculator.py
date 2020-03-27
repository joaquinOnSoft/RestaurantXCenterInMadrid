import geopy.distance


class CentersToRestaurantDistanceCalculator:

    def __init__(self, centers, restaurants):
        self.centers = centers
        self.restaurants = restaurants

    def calculate(self):
        centers_extended_info = []

        for center in self.centers:
            min_distance = 1000000000
            nearest_restaurant = None

            print(center["CODIGO CENTRO"], center["CENTRO"])

            for restaurant in self.restaurants:
                if center["lat"] is not None and center["lat"] != "":
                    coordinates_center = (float(center["lat"]), float(center["lng"]))
                else:
                    coordinates_center = (0.0, 0.0)

                if restaurant["latitude"] is not None and restaurant["latitude"] != "":
                    coordinates_restaurant = (float(restaurant["latitude"]), float(restaurant["longitude"]))
                else:
                    coordinates_restaurant = (0.0, 0.0)

                # Getting distance between two points based on latitude/longitude
                # https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
                dist = geopy.distance.vincenty(coordinates_center, coordinates_restaurant).kilometers

                if dist < min_distance:
                    min_distance = dist
                    nearest_restaurant = restaurant

            if nearest_restaurant is not None:
                center["restaurant"] = nearest_restaurant["address"]
                center["distance"] = min_distance
                centers_extended_info.append({
                    "﻿AREA TERRITORIAL": center["﻿AREA TERRITORIAL"],
                    "CODIGO CENTRO": center["CODIGO CENTRO"],
                    "TIPO DE CENTRO": center["TIPO DE CENTRO"],
                    "CENTRO": center["CENTRO"],
                    "DOMICILIO": center["DOMICILIO"],
                    "MUNICIPIO": center["MUNICIPIO"],
                    "DISTRITO MUNICIPAL": center["DISTRITO MUNICIPAL"],
                    "COD. POSTAL": center["COD. POSTAL"],
                    "TELEFONO": center["TELEFONO"],
                    "FAX": center["FAX"],
                    "TITULARIDAD": center["TITULARIDAD"],
                    "URL": center["URL"],
                    "E-MAIL": center["E-MAIL"],
                    "restaurant (nearest)": nearest_restaurant["name"],
                    "restaurant address": nearest_restaurant["address"],
                    "restaurant latitude": nearest_restaurant["latitude"],
                    "restaurant longitude": nearest_restaurant["longitude"],
                    "distance (km)": min_distance})

        return centers_extended_info
