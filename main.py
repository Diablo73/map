import folium, pandas

map = folium.Map(location=[0, 0], zoom_start=2)

data = pandas.read_csv("Cric_Stad.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
city = list(data["CITY"])

fgc = folium.FeatureGroup(name="Cricket Stadiums")
for lt, ln, n, c in zip(lat, lon, name, city):
	fgc.add_child(folium.Marker(location=[lt, ln], radius=1, popup=n + ", " + c, icon=folium.Icon(color="lightgreen")))
print("Cricket Stadiums FILE DONE.......")

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'blue' if x['properties']['POP2005'] < 10000000
else 'yellow' if x['properties']['POP2005'] < 50000000 else 'green' if x['properties']['POP2005'] < 100000000 else 'red' if x['properties']['POP2005'] < 500000000 else 'black'}))
print("Population FILE DONE.......")

data = pandas.read_csv("Ap_Data.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
typ = list(data["TYPE"])
country = list(data["COUNTRY"])
city = list(data["CITY"])
iata = list(data["IATA"])

fgam = folium.FeatureGroup(name="Medium Airports", show=False)
fgal = folium.FeatureGroup(name="Large Airports", show=False)
for lt, ln, n, t, cou, ci, i in zip(lat, lon, name, typ, country, city, iata):
	if t == "MED":
		fgam.add_child(folium.Marker(location=[lt, ln], radius=0.20, popup=n + "(" + i + "), " + ci + ", " + str(cou), icon=folium.Icon(color="lightblue")))
	elif t == "LAR":
		fgal.add_child(folium.Marker(location=[lt, ln], radius=0.75, popup=n + "(" + i + "), " + ci + ", " + str(cou), icon=folium.Icon(color="lightred")))
	else:
		print("Check your Airport")
print("Airports FILE DONE.......")

print()
map.add_child(fgc)
print("Cricket Stadiums HTML ADDED.......")
map.add_child(fgp)
print("Population HTML ADDED.......")
map.add_child(fgam)
print("Airports(m) HTML ADDED.......")
map.add_child(fgal)
print("Airports(l) HTML ADDED.......")
map.add_child(folium.LayerControl())
print("LayerControl HTML ADDED.......")

print()
map.save("Map.html")
print("Exported.......")
print(map)
print("FINISHED.......")