


import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_table

import pandas as pd
import numpy as np
import json
import dash

app = dash.Dash()


linkedin_img = "https://freepngimg.com/thumb/linkedin/11-2-linkedin-png.png"

# Section layout --------------------

layout = html.Div(
    [
        html.Div( 
            [
                html.Div(
                    [
                        html.Div(
                            'PROYECTO TEAM 76', 
                            className='mb-5 display-4 font-weight-bold text-home-title font-medium',
                        ),
                        html.Div(
                            [
                                html.P(
                                    """
                                    Nuestro proyecto busca identificar y asignar rutas NA mediante una Convolutional Neural Network, un modelo matemático que se utiliza principalmente en el reconocimiento de imágenes. 
                    
                                    """, 
                                    className='lead font-weight-normal text-dark font-home-m'
                                ),

                                html.P(
                                    """
                                    
                                   El modelo toma los puntos de las coordenadas enviadas por un autobús en un viaje, luego los dibuja sobre un lienzo blanco para tener una imagen del viaje y se repite este proceso a varias rutas para generar el banco de imágenes que permite entrenar nuestro modelo y asignar rutas con gran precisión.  
                                    """, 
                                    className='lead font-weight-normal text-dark font-home-m'
                                ),
                                
                                        html.Div(
                                            [
                                                html.Img(src=app.get_asset_url('cnnproj.png'), className='div-for-image-ocp')
                                            ],
                                            className='col'
                                        ),
                                 
                            ],
                            className='mb-5',
                        ),
                       
                    ],
                    className='col-md-8 p-lg-5 mx-auto my-5',
                ),
            ],
            className = 'position-relative overflow-hidden text-center back-home',
        ),
        html.Hr(),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            'ALIADO', 
                            className='row mb-2 display-4 font-weight-bold text-home-title mx-auto justify-content-center font-medium',
                        ),
                        html.Div(
                            'GTPC - Area Metropolitana', 
                            className='col-sm mx-auto justify-content-center text-home-subitle',
                        ),

                        
                    ],
                    className = 'container pt-5 mt-2'
                ),



                html.Div(
                    [
                        
                    
                        html.Div(
                            [
                                html.A(
                                    [
                                        html.Div(
                                            [
                                                html.Img(src=app.get_asset_url('imagengtpc.jpeg'), className='div-for-image-ocp')
                                            ],
                                            className='col-sm'
                                        ),
                                    ],
                                    href="https://www.metropol.gov.co/",
                                ),
                               
                            ],
                            className='col-md-3 offset-md-3'
                        ),


                        html.Div(
                            [
                                html.P(
                                    """
                                    
                                   Desde Área Metropolitana del Valle de Aburrá, partiendo del compromiso que como autoridad de transporte público y ambiental hemos asumido por mejorar la ​calidad del aire del territorio y por optimizar la operación del servicio de transporte público de la región, estamos trabajando en modernizar la flota de buses y la implementación de un sistema para su gestión y control. 
                                    """, 
                                    className='lead font-weight-normal text-dark font-home-m'
                                ),
                               
                            ],
                            className='col-md-5'
                        ),
                    ],
                    className = 'row p-lg-8 mx-auto my-8'
                ),
            
            ],
            className = 'position-relative overflow-hidden text-center',
            id='aliados'
        ),
        html.Hr(),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            'QUIENES SOMOS', 
                            className='row mb-2 display-4 font-weight-bold text-home-title mx-auto justify-content-center font-medium',
                        ),
                        html.Div(
                            'Integrantes del equipo', 
                            className='row mx-auto justify-content-center text-home-paragraph',
                        ),
                    ],
                    className = 'container pt-5 mt-2'
                ),
              html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                [
                                    html.Div(
                                        [
                                            html.Img(src=app.get_asset_url('DianaMoreno.jpg'), className="member-picture"),
                                            html.Div('Diana Moreno', className='font-weight-bold text-names-team font-medium'),
                                            html.Div('Matemática y magíster en Estadística', className='text-subtitle-team'),
                                            html.A(
                                                # Use row and col to control vertical alignment of logo / brand
                                                html.Div(
                                                    [
                                                        html.Img(src=linkedin_img, height="25px", className="linkedin_icon"),
                                                    ],                                                    
                                                ),
                                                href="https://www.linkedin.com/in/diana-moreno-39391247/",
                                            ),
                                          ], className="col-md-12 div-for-member"),
                                        ],
                                        className='col col-md-3 col-sm-6 col-6 wrapper-member', 
                                    ),
                               
                                html.Div(
                                [
                                    html.Div(
                                        [
                                            html.Img(src=app.get_asset_url('AlejandroCano.jpeg'),className="member-picture"),
                                            html.Div('Alejandro Cano', className='font-weight-bold text-names-team font-medium'),
                                            html.Div('Economista', className='text-subtitle-team'),
                                            html.A(
                                                # Use row and col to control vertical alignment of logo / brand
                                                html.Div(
                                                    [
                                                        html.Img(src=linkedin_img, height="25px", className="linkedin_icon"),
                                                    ],                                                    
                                                ),
                                                href="https://www.linkedin.com/in/mauricioacano/",
                                            ),
                                          ], className="col-md-12  div-for-member"),
                                        ],
                                        className='col col-md-3 col-sm-6 col-6 wrapper-member col-6', 
                                    ),
                               
                                html.Div(
                                [
                                    html.Div(
                                        [
                                            html.Img(src=app.get_asset_url('GustavoGarcia.png'),className="member-picture"),
                                            html.Div('Gustavo Garcia', className='font-weight-bold text-names-team font-medium'),
                                            html.Div('Estadístico', className='text-subtitle-team'),
                                            html.A(
                                                # Use row and col to control vertical alignment of logo / brand
                                                html.Div(
                                                    [
                                                        html.Img(src=linkedin_img, height="25px", className="linkedin_icon"),
                                                    ],                                                    
                                                ),
                                                href="https://www.linkedin.com/in/gustavo-garcía-gómez-60a12569",
                                            ),
                                        ], className="col-md-12  div-for-member"),

                                    ],
                                    className='col col-md-3 col-sm-6 col-6 wrapper-member', 
                                ),
                                                            
                               
                     
                     
                                html.Div(
                                    [
                                    html.Div(
                                        [
                                            html.Img(src=app.get_asset_url('DavidAcosta.jpg'),className="member-picture"),
                                            html.Div('David Acosta', className='font-weight-bold text-names-team font-medium'),
                                            html.Div('Candidato a Ph.D. en Ingeniería Mecánica.', className='text-subtitle-team'),
                                            html.A(
                                                # Use row and col to control vertical alignment of logo / brand
                                                html.Div(
                                                    [
                                                        html.Img(src=linkedin_img, height="25px", className="linkedin_icon"),
                                                    ],                                                    
                                                ),
                                                href="https://www.linkedin.com/in/david-acosta-v",
                                            ),
                                        ], className="col-md-12  div-for-member"),
                                    ],
                                    className='col col-md-3 col-sm-6 col-6 wrapper-member', 
                                ),
                                
                                html.Div(
                                [
                                    html.Div(
                                        [
                                            html.Img(src=app.get_asset_url('SebastianChaves.jpeg'),className="member-picture"),
                                            html.Div('Sebastian Chaves', className='font-weight-bold text-names-team font-medium'),
                                            html.Div('Ingeniero de Sistemas y Computación', className='text-subtitle-team'),
                                            html.A(
                                                # Use row and col to control vertical alignment of logo / brand
                                                html.Div(
                                                    [
                                                        html.Img(src=linkedin_img, height="25px", className="linkedin_icon"),
                                                    ],                                                    
                                                ),
                                                href="https://www.linkedin.com/in/jschavesr",
                                            ),
                                    ], className="col-md-12  div-for-member"),
                                ],
                                className='col col-md-3 offset-md-2 col-sm-6 col-6 wrapper-member'), 
                                
                                html.Div(
                                [

                                    html.Div(
                                        [
                                            html.Img(src=app.get_asset_url('CristianSanchez.jpg'),className="member-picture"),
                                            html.Div('Cristian Sanchez', className='font-weight-bold text-names-team font-medium'),
                                            html.Div('Ingeniero Electrónico y Matemático', className='text-subtitle-team'),
                                            html.A(
                                                # Use row and col to control vertical alignment of logo / brand
                                                html.Div(
                                                    [
                                                        html.Img(src=linkedin_img, height="25px", className="linkedin_icon"),
                                                    ],                                                    
                                                ),
                                                href="#",
                                            ),
                                        ], className="col-md-12 div-for-member"),
                                    ],
                                    className='col col-md-3 col-sm-6 col-6 wrapper-member', 
                                ),                         
                                html.Div(
                                [

                                    html.Div(
                                        [
                                            html.Img(src=app.get_asset_url('RubenBetancur.jpeg'),className="member-picture"),
                                            html.Div('Ruben Betancur', className='font-weight-bold text-names-team font-medium'),
                                            html.Div('Filósofo y MSc en Gestión Tecnológica', className='text-subtitle-team'),
                                            html.A(
                                                # Use row and col to control vertical alignment of logo / brand
                                                html.Div(
                                                    [
                                                        html.Img(src=linkedin_img, height="25px", className="linkedin_icon"),
                                                    ],                                                    
                                                ),
                                                href="#",
                                            ),
                                        ], className="col-md-12  div-for-member"),
                                    ],
                                    className='col col-md-3 col-sm-6 col-6 wrapper-member', 
                                ),
                                
                               
                            ],
                            className='row',
                        ),

                        
                            
    
                        
                    ],
                    className = 'container pt-5 mt-2 mb-5 d-flex justify-content-center'
                ),
            ],
            className = 'position-relative overflow-hidden text-center div-for-quienes-somos',
        ),
        html.Hr(),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            'CONTACTO', 
                            className='row mb-2 display-4 font-weight-bold text-home-title mx-auto justify-content-center font-medium',
                        ),
                        html.Div(
                            'team76ds4a@gmail.com', 
                            className='row mx-auto justify-content-center pt-4 text-home-paragraph',
                        ),
                        
                    ],
                    className = 'container py-5 mt-2'
                ),
            ],
            className = 'position-relative overflow-hidden text-center pb-2',
        ),

       

    ]
)
