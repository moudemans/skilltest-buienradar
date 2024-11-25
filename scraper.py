import json
import urllib.request

# Simple function which retrieves the json data from buienradar
def scrape() -> json:
    #  TODO: Check site availability?
    # TODO: Check data?
    with urllib.request.urlopen("https://data.buienradar.nl/2.0/feed/json") as url:
        data = json.load(url)
        return data