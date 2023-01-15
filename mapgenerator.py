import folium
import webbrowser
import os


def generate_map(src,dst):

    source = src
    destination = dst

    MAP = folium.Map(location=[34.0691,72.6441],zoom_start= 20) #loading static map

    temp = os.path.join('C:/Users/LENOVO/Desktop/dsa proj/ProjectRoutesPERSON/ProjectRoutesPERSON/from'+source+'/'+source+'to'+destination+'.txt')
    folium.GeoJson(temp, name = source+'to'+destination).add_to(MAP)

    MAP.save("intial.html")

def open_map():
    webbrowser.open_new_tab('C:/Users/LENOVO/Desktop/dsa proj/intial.html')
