# %%
import pandas as pd

from dash import Dash, html, dcc, dash_table
from dash_bootstrap_components.themes import SUPERHERO
import dash_bootstrap_components as dbc

from . import outlier_checkbox
from . import category_dropdown
from . import date_range
from . import sales_filter
from . import price_filter
from . import review_filter
from. import product_include_filter
from . import total_products
from . import sales_median
from . import price_median
from . import data_table
from . import histogram_selection
from . import histogram_selection_2
from . import histogram
from . import revenue_review
from . import ids



def create_layout(app:Dash, data: pd.DataFrame) -> html.Div:
    return dbc.Container(
                                [
                                 # Title head
                                 dbc.Row(
                                                [
                                                 html.H1(app.title), 
                                                 html.Hr()
                                                ],
                                                 className = "text-center border-0",
                                                 justify="center"
                                         ),
                                 # Critera Section
                                 dbc.Row(
                                         
                                                [
                                                 dbc.Col(
                                                         dbc.Card(
                                                                  [
                                                                   outlier_checkbox.render(app, data)
                                                                  ],
                                                                  body = True,
                                                                  className = "shadow-lg rounded align-middle text-sm-center" 
                                                                ),
                                                         width = 1,
                                                         align="center"
                                                        ),
                                                 dbc.Col(
                                                         dbc.Card(
                                                                 [
                                                                  category_dropdown.render(app, data)
                                                                 ],
                                                                 body = True,
                                                                 className = "shadow-lg rounded align-middle text-sm-center" 
                                                                 ),
                                                         #width = 3,
                                                         align="center",
                                                         ),
                                                 dbc.Col(
                                                         
                                                          dbc.Card(
                                                                   [
                                                                    date_range.render(app)
                                                                    ],
                                                                   body = True,
                                                                   className = "shadow-lg rounded align-middle text-sm-center" 
                                                                   ),
                                                          width = 2,
                                                          align = "center"
                                                         )
                                                 
                                                ], 
                                                justify="center"              
                                         ),
                                html.Hr(),
                                # Column Filters
                                dbc.Row(
                                         
                                                [
                                                 dbc.Col(
                                                          
                                                           dbc.Card(
                                                                    [
                                                                     product_include_filter.render(app)
                                                                     ],
                                                                    body = True,
                                                                    className = "shadow-lg rounded align-middle text-sm-center" 
                                                                    ),
                                                            width = 2,
                                                            align="center"
                                                           
                                                          ),
                                                 dbc.Col(
                                                         
                                                          dbc.Card(
                                                                   [
                                                                    sales_filter.render(app)
                                                                    ],
                                                                   body = True,
                                                                   className = "shadow-lg rounded align-middle text-sm-center" 
                                                                   ),
                                                           width = 2,
                                                           align="center"
                                                          
                                                         ),
                                                 dbc.Col(
                                                         
                                                          dbc.Card(
                                                                   [
                                                                    review_filter.render(app)
                                                                    ],
                                                                   body = True,
                                                                   className = "shadow-lg rounded align-middle text-sm-center" 
                                                                   ),
                                                           width = 2,
                                                           align="center"
                                                          
                                                         ),
                                                 dbc.Col(
                                                          
                                                           dbc.Card(
                                                                    [
                                                                     price_filter.render(app)
                                                                     ],
                                                                    body = True,
                                                                    className = "shadow-lg rounded align-middle text-sm-center" 
                                                                    ),
                                                            width = 2,
                                                            align="center"
                                                           
                                                          )
                                                 
                                                ], 
                                                justify="center"              
                                         ),
                                html.Hr(),
                                html.Br(),
                                
                                # Table Numbers
                                 dcc.Store(id = ids.STORE_DATA),        
                                 dbc.Row(
                                         [
                                          dbc.Col(
                                                  dbc.Card(
                                                           [
                                                           dbc.CardBody(
                                                                           [
                                                                                   html.H3("Total Products"),
                                                                                   total_products.render(app)
                                                                           ]
                                                                           
                                                                           #className = "shadow-lg rounded align-middle"
                                                                           ),
                                                           ],
                                                           class_name = "shadow-lg rounded align-middle text-sm-center" 
                                                           ),
                                                           width = 2,
                                                           align="center"
                                                 ),
                                         dbc.Col(
                                                         dbc.Card(
                                                                 [
                                                                 
                                                                 dbc.CardBody(
                                                                                 [
                                                                                         html.H3("Sales Median"),
                                                                                         sales_median.render(app)
                                                                                 ]
                                                                                 
                                                                                 #className = "shadow-lg rounded align-middle"
                                                                                 ),
                                                                 ],
                                                                 class_name = "shadow-lg rounded align-middle text-sm-center" 
                                                         ),
                                                         width = 2,
                                                         align="center"
                                                 ),
                                         dbc.Col(
                                                         dbc.Card(
                                                                 [
                                                                 
                                                                 dbc.CardBody(
                                                                                 [
                                                                                         html.H3("Price Median"),
                                                                                         price_median.render(app)
                                                                                 ]
                                                                                 
                                                                                 #className = "shadow-lg rounded align-middle"
                                                                                 ),
                                                                 ],
                                                                 class_name = "shadow-lg rounded align-middle text-sm-center" 
                                                         ),
                                                         width = 2,
                                                         align="center"
                                                 ),    
                                         ], 
                                         justify="center"              
                                         ),
                                 
                                 ### Graphs
                                 dbc.Row(
                                         [
                                          dbc.Col(
                                                  dbc.Card(
                                                          [
                                                           dbc.Row(
                                                                   [
                                                                    dbc.Col(
                                                                            [
                                                                            histogram_selection.render(app)
                                                                            ]
                                                                            ),
                                                                    dbc.Col(
                                                                            [
                                                                            histogram_selection_2.render(app)
                                                                            ]
                                                                            )        
                                                                    ]
                                                                   ),
                                                           
                                                            histogram.render(app)
                                                           ],
                                                           body = True,
                                                           className = "shadow-lg rounded p-auto"
                                                          ),
                                                  #width = 2,
                                                  align="center",
                                                  #className = "w-25 mb-3"
                                                 ),
                                           dbc.Col(
                                                  dbc.Card(
                                                           [
                                                            revenue_review.render(app)
                                                           ],
                                                           body = True,
                                                           className = "shadow-lg rounded p-auto"
                                                          ),
                                                  #width = 2,
                                                  align="center",
                                                  #className = "w-25 mb-3"
                                                 )
                                         ],  
                                         justify="center"                
                                        ),
                                 html.Hr(),
                                 ### Stats Table
                                 dbc.Row(
                                         [
                                          dbc.Col(
                                                  dbc.Card(
                                                           [
                                                            data_table.render(app, data)
                                                           ],
                                                           body = True,
                                                           className = "shadow-lg rounded p-auto"
                                                          ),
                                                  #width = 5,
                                                  align="center",
                                                  className = "w-75 mb-3"
                                                  )
                                         ],  
                                         justify="center"                
                                        ),
                                 html.Br(),
                                 html.Br(),
                                 # Graphs
                                 
                                 html.Br(),
                                 html.Br(),

                                ],

                        className = "bg-light bg-gradient w-100",
                        fluid = True
                        )