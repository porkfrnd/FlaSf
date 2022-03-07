import geocoder
import folium


g = geocoder.ip(input("ur ip"))

myadress = g.latlng
mymap_1 = folium.Map(location=myadress,
                     zoom_start=12)

mymap_1.save("my_map.html ")


print(f"Latitude And Longitude:{myadress}")
