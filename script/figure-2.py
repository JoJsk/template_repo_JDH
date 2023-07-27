import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.default = 'notebook'

# Data for the pie chart
labels = ['Austria', 'Poland', 'Ukraine','Romania', 'Hungary', 'Croatia', 'Serbia', 'Slovenia','Italy','Slovakia', 'Czech Republic', 'Bosnia and Herzegovina']
values = [29, 13, 11, 10, 8, 7, 6, 5, 3, 3, 3, 2]

# Create the pie chart figure
fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

# Set the layout
fig.update_layout(title='Distribution of Citizen Scientists by Country (in %)')

# Set the font color to white
fig.update_traces(textfont_color='white')

# Display the chart
fig.show()