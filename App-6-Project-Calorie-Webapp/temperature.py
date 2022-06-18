from bs4 import BeautifulSoup
import requests

class Temperature:
    """
    Represents the temperature given a location (country and city)
    Extracted from timeanddate.com/weather
    """
    base_url = 'https://www.timeanddate.com/weather/'

    def __init__(self, country, city):
        self.country = country
        self.city = city

    def _build_url(self):
        """Builds url using city and country"""
        url = self.base_url + self.country + '/' + self.city
        return url

    def _scrape(self):
        request = requests.get(self._build_url())
        content = request.text

        soup = BeautifulSoup(content, 'html.parser')
        text_filtered = soup.find(id='qlook')
        raw_result = BeautifulSoup(str(text_filtered), 'html.parser').find('div', attrs={'class': 'h2'}).text

        return raw_result

    def get(self):
        raw_result = self._scrape()
        result = raw_result.replace('\xa0°C', '')

        return result


if __name__ == "__main__":
    temperature = Temperature(city='barcelona', country='spain')
    print(temperature.get())