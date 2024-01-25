import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk


#filter= data[data[DATE_COLUMN].dt.hour == hour_to_filter]#
min_value = 1
max_value = 25

def Total(p):
    del(p['Comércio'])
    del(p['Casa'])
    del(p['Plantação'])
    del(p['Sitio'])
    return p

def Comercio(p):
    del(p['Total'])
    del(p['Casa'])
    del(p['Plantação'])
    del(p['Sitio'])
    return p

def Casa(p):
    del(p['Comércio'])
    del(p['Total'])
    del(p['Plantação'])
    del(p['Sitio'])
    return p

def Plantacao(p):
    del(p['Comércio'])
    del(p['Casa'])
    del(p['Total'])
    del(p['Sitio'])
    return p

def Sitio(p):
    del(p['Comércio'])
    del(p['Casa'])
    del(p['Plantação'])
    del(p['Total'])
    return p




def principal():
       
    chart_data = filtrado
    

    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=-23.50798,
            longitude=-46.55123,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
               'HeatmapLayer',
               data=chart_data,
               get_position='[LON, LAT]',
               radius=200,
               elevation_scale=100,
               elevation_range=[1,30],
               pickable=True,
               extruded=True,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=chart_data,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
            ),
        ],))
 


DATA_URL = 'InfoInvasao.xlsx'
arq = pd.read_excel(DATA_URL)


    
option = st.sidebar.selectbox(
"Que tipo de propriedade você deseja verificar?",
("Total","Comércio","Casa","Plantação","Sitio"))


values = st.sidebar.slider(
'Selecionar um intervalo de quantidade de propriedades',
1, 30, (1, 30))

if (option == 'Total'):
    arq = Total(arq)
elif (option == 'Casa'):
    arq = Casa(arq)
elif (option == 'Plantação'):
    arq = Plantacao(arq)
elif (option == 'Sitio'):
    arq = Sitio(arq)
elif (option == 'Comércio'):
    arq = Comercio(arq)

 

filtrado1 = arq[arq[str(option)]>=values[0]]
filtrado2 = filtrado1[filtrado1[str(option)]<=values[1]]
filtrado = filtrado2


if st.sidebar.button('Iniciar'):
   principal()

if st.sidebar.button('Exemplo km 40'):
    st.subheader('Video Arquivo SketchUp km 42')
    video_file = open('km 42.mp4','rb')
    video_bytes = video_file.read()
    st.video(video_bytes)






