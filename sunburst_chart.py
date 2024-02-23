import plotly.express as px

'''Simple Data:'''
data = {
    'id': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'parent': ['', 'A', 'A', 'B', 'B', 'C', 'D'],
    'value': [20, 12, 7, 17, 33, 27]
}

'''Create the Sunburst chart'''
fig = px.sunburst(data, names='id', parents='parent', values='value')

'''Set chart title'''
fig.update_layout(title_text= 'Sunburst Chart')

'''Show the chart'''
fig.show()