import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables ######

myheading = "Scoring Averages for the top 3 players in NBA over past 5 years"
mytitle = "Scoring Averages for the top 3 players in NBA over past 5 years"
x_values = ['2015', '2016', '2017', '2018', '2019']
y1_values = [25.3, 25.3, 26.4, 27.5, 27.4]
y2_values = [300, 306, 353, 365, 304, 285]
y3_values = [27.4, 29.0, 29.1, 30.4, 36.1]
y4_values = [23.8, 30.1, 25.3, 26.4, 27.3]
color1 = '#f5f542'
color2 = '#ff0303'
color3 = '#000000'
color4 = '#03cffc'
name1 = 'Lebron James'
name2 = 'Kevin Durant'
name3 = 'James Harden'
name4 = 'Stephen Curry'

tabtitle = 'basketball'
sourceurl = 'https://www.basketball-reference.com'
githublink = 'https://github.com/austinlasseter/dash-linechart-example'

########### Set up the chart

# create traces
trace0 = go.Scatter(
    x = x_values,
    y = y1_values,
    mode = 'lines',
    marker = {'color': color1},
    name = name1
)
trace1 = go.Scatter(
    x = x_values,
    y = y2_values,
    mode = 'lines',
    marker = {'color': color2},
    name = name2
)
trace2 = go.Scatter(
    x = x_values,
    y = y3_values,
    mode = 'lines',
    marker = {'color': color3},
    name = name3
)

trace2 = go.Scatter(
    x = x_values,
    y = y4_values,
    mode = 'lines',
    marker = {'color': color4},
    name = name4
)


# assign traces to data
data = [trace0, trace1, trace2]
layout = go.Layout(
    title = mytitle
)

# Generate the figure dictionary
fig = go.Figure(data=data,layout=layout)

########### Initiate the app
app = dash.Dash()
server = app.server
app.title=tabtitle
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
