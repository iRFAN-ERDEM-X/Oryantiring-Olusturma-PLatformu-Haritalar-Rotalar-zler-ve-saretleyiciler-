import folium
from folium import IFrame
import os
import base64
from geopy.distance import distance
import requests
from pprint import pprint

location = float(41.001702702786055), float(28.694652915000916)
location2 = float(41.00406292033456), float(28.69100511074066)
km = distance(location, location2)
print("Distance between postcodes:")
print(f"{km}")


m = folium.Map(location=[41.0049,28.6934], zoom_start=16)
walkData = os.path.join('walk.json')

folium.GeoJson(walkData, name='walk').add_to(m)

folium.PolyLine([(41.001702702786055, 28.694652915000916), (41.00406292033456, 28.69100511074066)], color="red", weight=4).add_to(m)



tooltip = "Click to see picture"
html = '<img src="data:image/png;base64,{}">'.format

picture1 = base64.b64encode(open('./images/1.png','rb').read()).decode()
iframe1 = IFrame(html(picture1), width=600+20, height=600+20)
popup1 = folium.Popup(iframe1, max_width=650)
icon1 = folium.features.CustomIcon('logo2.png', icon_size=(30,30))
marker1 = folium.Marker(location=[41.001702702786055,  28.694652915000916], popup=popup1, tooltip=tooltip, icon=icon1).add_to(m)

picture2 = base64.b64encode(open('./images/2.png','rb').read()).decode()
iframe2 = IFrame(html(picture2), width=600+20, height=600+20)
popup2 = folium.Popup(iframe2, max_width=650)
icon2 = folium.Icon(color="blue", icon="glyphicon-home")
marker2 = folium.Marker(location=[41.00215613021236,  28.694411516189575], popup=popup2, tooltip=tooltip, icon=icon2).add_to(m)

picture3 = base64.b64encode(open('./images/3.png','rb').read()).decode()
iframe3 = IFrame(html(picture3), width=600+20, height=600+20)
popup3 = folium.Popup(iframe3, max_width=650)
icon3 = folium.Icon(color="red", icon="glyphicon-home")
marker3 = folium.Marker(location=[41.002504295583094, 28.694497346878055], popup=popup3, tooltip=tooltip, icon=icon3).add_to(m)

picture4 = base64.b64encode(open('./images/4.png','rb').read()).decode()
iframe4 = IFrame(html(picture4), width=600+20, height=600+20)
popup4 = folium.Popup(iframe4, max_width=650)
icon4 = folium.Icon(color="green", icon="glyphicon-home")
marker4 = folium.Marker(location=[41.00371881154719, 28.691702485084534], popup=popup4, tooltip=tooltip, icon=icon4).add_to(m)

picture5 = base64.b64encode(open('./images/8.png','rb').read()).decode()
iframe5 = IFrame(html(picture5), width=600+20, height=600+20)
popup5 = folium.Popup(iframe5, max_width=650)
icon5 = folium.Icon(color="red", icon="glyphicon-home")
marker5 = folium.Marker(location=[41.00406292033456, 28.69100511074066], popup=popup5, tooltip=tooltip, icon=icon5).add_to(m)

picture6 = base64.b64encode(open('./images/9.png','rb').read()).decode()
iframe6 = IFrame(html(picture6), width=600+20, height=600+20)
popup6 = folium.Popup(iframe6, max_width=650)
icon6 = folium.Icon(color="red", icon="glyphicon-home")
marker6 = folium.Marker(location=[41.004605394068015, 28.690431118011475], popup=popup6, tooltip=tooltip, icon=icon6).add_to(m)

picture7 = base64.b64encode(open('./images/11.png','rb').read()).decode()
iframe7 = IFrame(html(picture7), width=600+20, height=600+20)
popup7 = folium.Popup(iframe7, max_width=650)
icon7 = folium.Icon(color="red", icon="glyphicon-home")
marker7 = folium.Marker(location=[41.00204277364823, 28.69675576686859], popup=popup7, tooltip=tooltip, icon=icon7).add_to(m)

picture8 = base64.b64encode(open('./images/7.png','rb').read()).decode()
iframe8 = IFrame(html(picture8), width=600+20, height=600+20)
popup8 = folium.Popup(iframe8, max_width=650)
icon8 = folium.Icon(color="red", icon="glyphicon-home")
marker8 = folium.Marker(location=[41.00661736586017, 28.69126796722412], popup=popup8, tooltip=tooltip, icon=icon8).add_to(m)

picture9 = base64.b64encode(open('./images/12.png','rb').read()).decode()
iframe9 = IFrame(html(picture9), width=600+20, height=600+20)
popup9 = folium.Popup(iframe9, max_width=650)
icon9 = folium.Icon(color="red", icon="glyphicon-home")
marker9 = folium.Marker(location=[41.00434225438185, 28.693370819091797], popup=popup9, tooltip=tooltip, icon=icon9).add_to(m)


m.save("index.html")
