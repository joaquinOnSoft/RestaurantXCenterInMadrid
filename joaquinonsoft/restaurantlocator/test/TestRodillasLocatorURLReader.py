from unittest import TestCase

from ..RodillasLocatorURLReader import RodillasLocatorURLReader


class TestRodillasLocatorURLReader(TestCase):

    def test_read(self):
        locator = RodillasLocatorURLReader()
        response = locator.read()

        self.assertIsNotNone(response)
        self.assertEqual(98, len(response))

        restaurant = response[0]
        self.assertEqual("VIPS Sol", restaurant["name"])
        self.assertEqual("40.416727", restaurant["latitude"])
        self.assertEqual("-3.703387", restaurant["longitude"])
        self.assertEqual("Puerta del Sol, 3 Madrid", restaurant["address"])
        self.assertEqual("669148462", restaurant["phone"])
