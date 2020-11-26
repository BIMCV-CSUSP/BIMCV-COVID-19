#!/usr/bin/env python
# coding: utf-8


import os

import pandas as pd
import geopandas as gpd
from math import isnan


# import numpy as np
from geopy.geocoders import Nominatim  # get location coordinates
import folium
from folium import plugins
from branca.colormap import LinearColormap

# ruta absoluta para evitar problemas por desplazamiento
wd = r'C:\*****\Lna\******\******\Mapas\Lna_modificado'

# Importamos el csv como dataframe. 


#inputfile con los datos positivos covid19 iter 1 y 2:
df = pd.read_csv(os.path.join(wd,"data","MAP_INFO_GENERAL_RESUMEN_DEP_ITER1_2.csv"), sep=';', dtype={'DEPARTAMENTO':str})

df.head()


# Importamos el fichero GeoJSON como dataframe gracias a la libreria `geopandas`.


limits = gpd.read_file(os.path.join(wd,"data","departamentos_salud_ogr.json"))



limits.head()


# A los ID de Departamentos y zonas de nuestro csv sintetico con un solo digito les falta un 0 a la izquierda.
# Se lo anyadimos con apply.



df['DPTOCRC'] = df['DEPARTAMENTO'].apply(lambda x: '0' + x if len(x) == 1 else x)
#En caso de que números entre comillas: df['DPTOCRC'] = df['DEPARTAMENTO'].apply(lambda x: '0' + str(x) if len(str(x)) == 1 else str(x))


#df = df.drop([0]) # elimino la fila 0




df.head()


# Unimos los dos dataframes usando el codigo de cuatro digitos de la zona como clave primaria


limits = limits.merge(df, how='inner', on='DPTOCRC')
#limits = df

#EOliver anyadido, poner columna con la suma de CR y DX
limits['n_CR_DX'] = limits['n_CR']+limits['n_DX']
#EOliver anyadido: Considerar 'NaN' como 0 en caso de que aparezca en los componentes de la suma
limits['n_CR_DX'] = limits['n_CR'].apply(lambda x: 0 if isnan(x) else x) + limits['n_DX'].apply(lambda x: 0 if isnan(x) else x)

limits.head()


# Podemos obtener las coordenadas de un punto central de la comunidad valenciana usando el geolocalizador `Nominatim`,
# de libre uso, contenido en la librería `Geopy`.


# Get geographical coordinate of CV
address = 'Comunitat Valenciana'
geolocator = Nominatim(user_agent="xbarber@umh.es")

location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print('The geographical coordinate of Comunitat Valenciana are {}, {}.'.format(latitude, longitude))

### Generacion del mapa


# En primero lugar, se genera el mapa centrado en las coordenadas indicadas y con un zoom inicial definido.
# Se indica que no anyada tiles inicialmente, asi podremos tener control de todo lo que se incluye en el mapa.
#  Despues se le anyade la tile layer "Light Map" `CartoDB positron`, porque es de libre acceso y muy aseptica a nivel visual.
#  Ademas, se incluye un plugin para poder visualizar el mapa a pantalla completa.



# create a plain world map Mapbox Bright ,'CartoDB positron'
m = folium.Map(location=[latitude, longitude], zoom_start=8, tiles=None) 
folium.TileLayer(tiles='OpenStreetMap',name="Light Map",control=False).add_to(m)

plugins.Fullscreen(
    position='topright',
    title='Expand me',
    title_cancel='Exit me',
    force_separate_button=True
).add_to(m)


# Se anyade la capa del mapa coropletico, que se colorea en funcion de una determinada variable.
# Para cada campo se incluye una explicacion.


df2=df.set_index('DPTOCRC')['n_CR'].to_dict()

color_scale = LinearColormap(['yellow','red'], vmin = min(df2.values()),
                                               vmax = max(df2.values()))

def get_color(feature):
    value = df2.get(feature['properties']['DPTOCRC'])
    if value is None:
        return '#8c8c8c'  # MISSING -> gray
    else:
        return color_scale(value)
    
    



folium.Choropleth(
geo_data=limits,  # Objeto en el cual estan incluidas las coordenadas
name='Health Dpt.',  # Nombre de la capa
data=limits,  # Objeto en el cual se encuentra la variable a representar. En este caso coincide que el objeto es el mismo
              # para la variable y las coordenadas, aunque podia no ser el caso.
columns=['DPTOCRC','n_CR'],  # En primer lugar se indica la columna con la clave que relaciona #'n_CR',
                                    # En segundo, la variable a representar
key_on="feature.properties.DPTOCRC",  # Localizacion del campo DEPTOCRC en el GeoJSON
fill_color='YlGnBu',  # Codigo de la paleta de colores
fill_opacity=0.8,  # Opacidad del relleno
line_opacity=0.5,  # Opacidad de los nombres
legend_name='Health Department with data',  # titulo de la leyenda
nan_fill_color='white',
highlight=True
).add_to(m)


# Se anyaden las style y highlight functions para resaltar una zona al pasar el raton por encima.
# Ademas, se incorporan cajas de texto que indican el valor de las variables que se quiera por zona senyalada.
# Por ultimo, se incorpora un control de capas para poder activar/desactivar los rellenos.



# convert to (n, 2) nd-array format for heatmap
#stationArr = limits[['latitude', 'longitude']].as_matrix()

#m.add_children(plugins.HeatMap(stationArr, radius=15))



style_function = lambda feature: {'fillColor': '#ffffff',  # get_color(feature),
                                  #'#ffffff', 
                            'color':'#000000', 
                            'fillOpacity': 0.1, 
                            'weight': 0.1}


highlight_function = lambda feature: {'fillColor': '#000000', # get_color(feature),
                                  # '#000000', 
                                'color':'#000000', 
                                'fillOpacity': 0.50, 
                                'weight': 0.1}    


f1 = folium.FeatureGroup(name='CR').add_to(m)

NIL = folium.features.GeoJson(
    limits,  # Dataframe con la variable a representar
    style_function=style_function, 
     control=False,
     name="CR number",
    highlight_function=highlight_function, 
    tooltip=folium.features.GeoJsonTooltip(  # Caja de texto
        fields=['DPTOCRC','NOMBRE','n_CR' ],  # Variables incluidas
        aliases=['Health department: ','Name: ','CR: '],  # Texto que precede a las variables
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;") 
    )
).add_to(f1)



f2 = folium.FeatureGroup(name='DX').add_to(m)



NIL2 = folium.features.GeoJson(
    limits,  # Dataframe con la variable a representar
    style_function=style_function, 
    control=False,
    name="DX number",
    highlight_function=highlight_function, 
    tooltip=folium.features.GeoJsonTooltip(  # Caja de texto
        fields=['DPTOCRC','NOMBRE', 'n_DX'],  # Variables incluidas
        aliases=['Health department: ','Name: ', 'DX'],  # Texto que precede a las variables
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;") 
    )
).add_to(f2)



f3 = folium.FeatureGroup(name='CR+DX').add_to(m)



NIL3 = folium.GeoJson(
    limits,  # Dataframe con la variable a representar
    style_function=style_function, 
    control=False,
    name="CR+DX number",
    highlight_function=highlight_function, 
    tooltip=folium.features.GeoJsonTooltip(  # Caja de texto
        fields=['DPTOCRC','NOMBRE', 'n_CR_DX'],  # Variables incluidas
        aliases=['Health department: ','Name: ', 'CR+DX'],  # Texto que precede a las variables
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;") 
    )
).add_to(f3)

f4 = folium.FeatureGroup(name='CT').add_to(m)



NIL4 = folium.GeoJson(#. features.
    limits,  # Dataframe con la variable a representar
    name="CT number",
    #legend="Number of CT:",
    style_function=style_function, 
    control=False,
    highlight_function=highlight_function, 
    tooltip=folium.features.GeoJsonTooltip(  # Caja de texto
        fields=['DPTOCRC','NOMBRE', 'n_CT'],  # Variables incluidas
        aliases=['Health department: ','Name: ', 'CT'],  # Texto que precede a las variables
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;") 
    )
).add_to(f4)

folium.LayerControl().add_to(m)

 
#folium.LayerControl(autoZIndex=False, collapsed=True).add_to(m)

#m.keep_in_front(NIL1, NIL2, NIL3, NIL4)

# m.add_child(NIL) # se anyade al mapa
# m.add_child(NIL2)
#  m.add_child(NIL3)
# m.add_child(NIL4)

#m.keep_in_front(NIL) # se lleva al frente para no quedar detras del mapa#
#m.add_child(folium.LayerControl())

#m.fit_bounds(NIL.get_bounds()) 

#folium.LayerControl().add_to(m)
#folium.LayerControl(collapsed=False).add_to(m)# control de capas para poder ocultar el relleno #collapsed=False

#m.add_child(NIL)

#m

#outputfile cambiado por EOliver por los nuevos datos
m.save(os.path.join(wd,"Departamentos3.html"))



