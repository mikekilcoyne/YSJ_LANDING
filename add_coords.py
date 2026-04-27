import json
import re

with open("../FIND_MY_BK_CLUB__main_recovery/data/clubs-map.json", "r") as f:
    map_data = json.load(f)

# Create a lookup
coords = {}
for c in map_data:
    city_name = c["city"].split(",")[0].strip().lower()
    coords[city_name] = {"lat": c["latitude"], "lng": c["longitude"]}

print(coords)

with open("breakfast-qwest.html", "r") as f:
    html = f.read()

# We need to find the clubData array and add lat/lng
import ast

# The clubData array starts at "const clubData = [" and ends at "].map((club) => ({"
match = re.search(r'const clubData = (\[.*?\])\.map', html, re.DOTALL)
if match:
    array_str = match.group(1)
    
    # We'll regex replace to inject lat/lng
    # Since its JS objects, we can parse it as JS. Let's do a quick regex injection per line
    lines = array_str.split("\n")
    out_lines = []
    for line in lines:
        if "{ city:" in line:
            # extract city
            city_match = re.search(r'city:\s*"([^"]+)"', line)
            if city_match:
                city = city_match.group(1)
                lookup = city.lower().split(",")[0].strip()
                if lookup == "maplewood" or lookup == "soma": lookup = "maplewood" # alias
                if lookup == "surf coast - torquay": lookup = "torquay"
                if lookup == "new york - hamptons": lookup = "new york - hamptons"
                # Some are exact, some might need adjustments
                lat, lng = None, None
                
                # Manual fallbacks
                if lookup.startswith('melbourne '):
                    if 'fitzroy' in lookup: lookup = 'melbourne - fitzroy'
                    elif 'richmond' in lookup: lookup = 'melbourne - richmond'
                elif lookup.startswith('new york '):
                    if 'brooklyn' in lookup: lookup = 'new york - downtown brooklyn'
                    elif 'upper' in lookup: lookup = 'new york - upper west'
                    elif 'hamptons' in lookup: lookup = 'new york - hamptons'
                    elif 'hudson' in lookup: lookup = 'new york - hudson'
                    elif 'kingston' in lookup: lookup = 'new york - kingston'
                    elif 'les' in lookup: lookup = 'new york - les'
                    elif 'williamsburg' in lookup: lookup = 'new york - williamsburg'
                    
                if lookup in coords:
                    lat, lng = coords[lookup]['lat'], coords[lookup]['lng']
                else:
                    # check if any starts with lookup
                    for k in coords:
                        if lookup in k:
                            lat = coords[k]['lat']
                            lng = coords[k]['lng']
                            break
                            
                if lat is not None:
                    # insert at end of object
                    line = line.replace('whatsapp: "" }', f'whatsapp: "", lat: {lat}, lng: {lng} }}')
                    line = line.replace('whatsapp: "https://chat.whatsapp.com/CW5dJN7RdcOGikCE8HLsdC?mode=gi_t" }', f'whatsapp: "https://chat.whatsapp.com/CW5dJN7RdcOGikCE8HLsdC?mode=gi_t", lat: {lat}, lng: {lng} }}')
                    line = line.replace('whatsapp: "https://chat.whatsapp.com/GQJQ41xFxzG7wA1RxNvU0H?mode=gi_t" }', f'whatsapp: "https://chat.whatsapp.com/GQJQ41xFxzG7wA1RxNvU0H?mode=gi_t", lat: {lat}, lng: {lng} }}')
                    line = line.replace('whatsapp: "https://chat.whatsapp.com/GWkWebokkQO6bMcynjSb4v?mode=gi_t" }', f'whatsapp: "https://chat.whatsapp.com/GWkWebokkQO6bMcynjSb4v?mode=gi_t", lat: {lat}, lng: {lng} }}')
                    line = line.replace('whatsapp: "https://chat.whatsapp.com/FzBGLGPTzG778Hwyk4ihcx" }', f'whatsapp: "https://chat.whatsapp.com/FzBGLGPTzG778Hwyk4ihcx", lat: {lat}, lng: {lng} }}')

        out_lines.append(line)
        
    new_html = html.replace(array_str, "\n".join(out_lines))
    with open("breakfast-qwest.html", "w") as f:
        f.write(new_html)
    print("Coordinates successfully added to clubData in breakfast-qwest.html")
else:
    print("Could not find clubData array")
