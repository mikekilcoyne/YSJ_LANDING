import urllib.request
import json
import time

cities = [
    "Amsterdam, Netherlands", "Atlanta, USA", "Austin, USA", "Barcelona, Spain",
    "Bassano del Grappa, Italy", "Berlin, Germany", "Biarritz, France", "Boston, USA",
    "Boulder, USA", "Brighton, UK", "Burlington, VT, USA", "Cambridge, MA, USA",
    "Chicago, USA", "Copenhagen, Denmark", "Denver, USA", "Ibiza, Spain",
    "London, UK", "Los Angeles, USA", "Lugano, Switzerland", "Manila, Philippines",
    "Melbourne, Australia", "Mexico City, Mexico", "Miami, USA", "Milano, Italy",
    "New York, USA", "Norwich, UK", "Panama City, Panama", "Paris, France",
    "Perth, Australia", "Philadelphia, USA", "Portland, ME, USA", "Portland, OR, USA",
    "San Francisco, USA", "Seattle, USA", "Singapore", "Maplewood, NJ, USA",
    "Torquay, Australia", "Sydney, Australia", "Toronto, Canada", "Las Vegas, USA",
    "Vienna, Austria", "Washington DC, USA", "Riyadh, Saudi Arabia"
]

coords = {}

for city in cities:
    try:
        url = "https://nominatim.openstreetmap.org/search?q=" + urllib.parse.quote(city) + "&format=json&limit=1"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            if data:
                coords[city] = {"lat": float(data[0]["lat"]), "lon": float(data[0]["lon"])}
                print(f"Got {city}: {coords[city]}")
            else:
                print(f"Failed {city}")
        time.sleep(1) # rate limit
    except Exception as e:
        print(f"Error {city}: {e}")

with open("coords.json", "w") as f:
    json.dump(coords, f, indent=2)
