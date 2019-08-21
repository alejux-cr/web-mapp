import folium
import pandas

volcano_data = pandas.read_csv("Volcanoes.txt")
lat = list(volcano_data["LAT"])
lon = list(volcano_data["LON"])
elev = list(volcano_data["ELEV"])

def color_points(p_el):
    if p_el < 1000:
        return 'green'
    elif 1000 <= p_el < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[9.99,-83.90], zoom_start=5, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.Marker(location=[lt,ln], popup=str(el)+" m", icon=folium.Icon(color=color_points(el))))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function = lambda x: {'fillColor':'orange'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Mapp.html")