import googlemaps

class ViennaScraper:
    def __init__(self, api_key):
        self.gmaps = googlemaps.Client(key=api_key)

    def get_vienna_clinics(self, query="Zahnarzt in Wien"):
        places_result = self.gmaps.places(query=query)
        clinics = []
        for place in places_result.get('results', []):
            name = place.get('name')
            rating = place.get('rating')
            clinics.append({"Name": name, "Rating": rating})
        return clinics