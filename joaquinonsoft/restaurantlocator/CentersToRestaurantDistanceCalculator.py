import geopy.distance


class CentersToRestaurantDistanceCalculator:

    def __init__(self, centers, restaurants):
        self.centers = centers
        self.restaurants = restaurants

    def calculate(self):
        for center in self.centers:
            min_distance = 1000000000
            nearest_restaurant = None

            for restaurant in self.restaurants:
                coordinates_center = (float(center["lat"]), float(center["lng"]))
                coordinates_restaurant = (float(restaurant["latitude"]), float(restaurant["longitude"]))

                print(coordinates_center)
                print(coordinates_restaurant)

                dist = geopy.distance.vincenty(coordinates_center, coordinates_restaurant).kilometers

                print(dist)

                if dist < min_distance:
                    min_distance = dist
                    nearest_restaurant = restaurant

            if nearest_restaurant is not None:
                center["restaurant"] = nearest_restaurant["address"]
                center["distance"] = min_distance

        return self.centers
