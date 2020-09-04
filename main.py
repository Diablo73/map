import folium, pandas

data = pandas.read_csv("Cric_Stad.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
city = list(data["CITY"])

map = folium.Map(location=[0, 0], zoom_start=2)

fgc = folium.FeatureGroup(name="Cricket Stadiums")
for lt, ln, n, c in zip(lat, lon, name, city):
    fgc.add_child(folium.Marker(location=[lt, ln], radius=1, popup=n + ", " + c, icon=folium.Icon(color="lightgreen")))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'blue' if x['properties']['POP2005'] < 10000000
else 'yellow' if x['properties']['POP2005'] < 50000000 else 'green' if x['properties']['POP2005'] < 100000000 else 'red' if x['properties']['POP2005'] < 500000000 else 'black'}))

map.add_child(fgc)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map.html")
print("Exported")
print(map)