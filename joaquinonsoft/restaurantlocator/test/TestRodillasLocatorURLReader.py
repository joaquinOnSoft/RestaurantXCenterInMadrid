from unittest import TestCase

from ..RodillasLocatorURLReader import RodillasLocatorURLReader


class TestRodillasLocatorURLReader(TestCase):

    def test_read(self):
        locator = RodillasLocatorURLReader()
        response = locator.read()

        self.assertIsNotNone(response)
        self.assertEqual(154, len(response))

        restaurant = response[0]
        self.assertEqual("Rodilla Kiosco Sol", restaurant["name"])
        self.assertEqual("40.41706", restaurant["latitude"])
        self.assertEqual("-3.702834", restaurant["longitude"])
        self.assertEqual("Est de Sol- Cercanías, plan -1, Stand E3, Prt  Sol, 28013, Madrid", restaurant["address"])
        self.assertEqual("", restaurant["phone"])
