import unittest

from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Does a simple city and country pair work?"""
        cape town_south africa = city_country('cape town', 'south africa')
print(city)
        self.assertEqual(cape town_south africa, 'Cape town', 'South africa')
print(city)

    def test_city_country_population(self):
        """Can I include a population argument?"""
        cape town_south africa = city_country('cape town', 'south africa', population=5_000_000)
        self.assertEqual(cape town_south africa, 'Cape town, South Africa - population 5000000')

if __name__ == '__main__':
    unittest.main()