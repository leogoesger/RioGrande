import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

py.sign_in('leogoesger', '9VqlPxirB4oFmaHW53Yu')

N = 500
random_x = np.linspace(0, 1, N)
random_y = np.random.randn(N)

# Create a trace
trace = go.Scatter(
    x = random_x,
    y = random_y
)

data = [trace]
py.image.save_as(data, filename='a-simple-plot.png')
# py.iplot(data, filename='basic-line')
