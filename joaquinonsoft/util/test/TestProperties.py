from unittest import TestCase

from joaquinonsoft.util.Properties import Properties


class TestProperties(TestCase):

    def test_read(self):
        prop = Properties("../../../resources/grant.properties")

        self.assertEqual(prop.get("test.prop"), "hola")
