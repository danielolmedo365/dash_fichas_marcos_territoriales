from dash import Dash, html, dcc
import plotly.graph_objs as go
import folium
from folium.plugins import MarkerCluster

# Datos ficticios
x_data = [1, 2, 3, 4]
y_data = [10, 11, 12, 13]


app = Dash(__name__)

# Crear un mapa de Folium
##############################################################################################
def create_folium_map():
    folium_map = folium.Map(location=[37.7749, -122.4194], zoom_start=10)

    marker_cluster = MarkerCluster().add_to(folium_map)
    folium.Marker([37.7749, -122.4194], popup='San Francisco').add_to(marker_cluster)
    folium.Marker([40.7128, -74.0060], popup='New York').add_to(marker_cluster)
    folium.Marker([34.0522, -118.2437], popup='Los Angeles').add_to(marker_cluster)
    folium.Marker([41.8781, -87.6298], popup='Chicago').add_to(marker_cluster)

    return folium_map
##############################################################################################





app.layout=html.Div([
    html.Div(children=[
        html.Label('Titulo')],style={   'text-align':'center',
                                         'font-size':'20px',
                                         'flexDirection':'column',
                                         'backgroundColor':'yellow',
                                         'width':'100%',
                                         'padding':'10px'}),
    html.Div(children=[
        html.Div([
            html.Label('Organización'),
            dcc.Dropdown(['SICOBI', 'CEDICAM', 'VICENTE GUERRERO', 'MAGUEYAL'],),
            html.Br(),
            
            
            html.Div([
                    dcc.Graph(
                        id='scatter-plot1',
                        figure={
                        'data': [go.Scatter(x=x_data, y=y_data, mode='markers')],
                        'layout': go.Layout(title='Scatter Plot1')
                        }
                    ),
                    
                    dcc.Graph(
                        id='scatter-plot2',
                        figure={
                        'data': [go.Scatter(x=x_data, y=y_data, mode='markers')],
                        'layout': go.Layout(title='Scatter Plot2')
                        }
                    ),
                    dcc.Graph(
                        id='scatter-plot3',
                        figure={
                        'data': [go.Scatter(x=x_data, y=y_data, mode='markers')],
                        'layout': go.Layout(title='Scatter Plot3')
                        }
                    ),
                    dcc.Graph(
                        id='scatter-plot4',
                        figure={
                        'data': [go.Scatter(x=x_data, y=y_data, mode='markers')],
                        'layout': go.Layout(title='Scatter Plot4')
                        }
                    ),
                    
                
                
            ], style={'display':'grid',
                      'grid-template-columns':'repeat(2,2fr)',
                      'grid-template-rows':'repeat(2, 2fr)',
                      'grid-gap':'5px',
                    'border-radius': '20px',  # Añadir esquinas redondeadas
                    'overflow': 'hidden',  # Ocultar cualquier desbordamiento
                    'background':"#c3c3c3",
                    'background': 'linear-gradient(to bottom rigth, #686868, #d0d0d5)',  # Agregar gradiente lineal


                      })            
            
            ],style={'text-align':'lefth',
                     'font-size':'20px',
                     'display':'flex',
                     'flexDirection':'column',
                     'width':'60%',
                     'padding':'20px'
                     

                     }),
                    
        html.Div([
            html.Label('Título del mapa'),
            html.Br(),            
            html.Iframe(
                id='folium-map',
                srcDoc=create_folium_map().get_root().render(),
                 style={'width': '100%', 'height': '100%', 'border-radius':'2%'}
                
                )
           
            
            ], style = {'font-size':'20px',
                        'display':'flex',
                        'flexDirection':'column',
                        'width':'40%',
                        'padding':'20px'
                        })
        
    ],style={'display':'flex',
             'flexDirection':'row',
             'padging':'10px',
             'background': 'linear-gradient(to bottom right, #f0f0f0, #d0d0d0)',  # Agregar gradiente lineal
            })
    
])
if __name__=='__main__':
    app.run(debug=True)
