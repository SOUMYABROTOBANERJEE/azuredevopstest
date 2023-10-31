import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load a sample dataset (you can replace this with your own data)
data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Data Analysis and Visualization"),
    
    # Data Selection
    html.Div([
        html.Label("Select Year:"),
        dcc.Dropdown(
            id='year-selector',
            options=[{'label': str(year), 'value': year} for year in data['year'].unique()],
            value=data['year'].max()
        ),
    ]),
    
    # Data Table
    html.Div(id='data-table'),

    # Data Filtering
    html.Div([
        html.Label("Select Continent(s):"),
        dcc.Dropdown(
            id='continent-selector',
            options=[{'label': continent, 'value': continent} for continent in data['continent'].unique()],
            multi=True,
            value=data['continent'].unique()
        ),
    ]),
    
    # Data Statistics
    html.Div(id='data-statistics'),

    # Data Visualization
    dcc.Graph(id='data-visualization'),

    # Interactive Component
    html.Div([
        html.Label("Select a Country:"),
        dcc.Dropdown(
            id='country-selector',
            options=[{'label': country, 'value': country} for country in data['country'].unique()],
        ),
        html.Div(id='selected-country'),
    ]),

    # Conclusion
    html.Hr(),
    html.H3("Conclusion"),
    html.Div("This is a Dash application with data analysis, visualization, and interactivity.")
])

@app.callback(
    Output('data-table', 'children'),
    Output('data-statistics', 'children'),
    Output('data-visualization', 'figure'),
    Output('selected-country', 'children'),
    Input('year-selector', 'value'),
    Input('continent-selector', 'value'),
    Input('country-selector', 'value')
)
def update_data(year, continents, selected_country):
    filtered_data = data[data['year'] == year]
    filtered_data = filtered_data[filtered_data['continent'].isin(continents)]
    
    data_table = html.Table(
        # Display data table here
    )
    
    data_statistics = html.Div(
        # Display statistics here
    )
    
    fig = px.scatter(
        filtered_data, x='gdpPercap', y='lifeExp',
        size='pop', color='country', hover_name='country', log_x=True, size_max=60
    )
    
    return data_table, data_statistics, fig, f"You selected {selected_country}"
server = app.server
if __name__ == '__main__':
    app.run_server(debug=True)
