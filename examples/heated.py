# Quick example to search for lots of materials and plot the youngs modulus
import os

# set user and password
os.environ["MATERIOM_USER"] = ''
os.environ["MATERIOM_PASSWORD"] = ''

from materpyom.read import materiom_search

import numpy as np
import plotly.graph_objects as go

# search for 'heated'
items = materiom_search('heated')
results = items['results']

youngs_moduluses = []
# get the youngs modulus of all the items
for result in results:

    try:
        name = print(result['content']['name'])

        youngs_modulus = result['content']['variableMeasured']['value']
        youngs_moduluses.append(youngs_modulus)

    except:
        pass

# plot using a box and diagram, use log scale as the young modulus varies a lot.
fig = go.Figure()
fig.add_trace(go.Box(x=np.log(youngs_moduluses), name=''))

fig.update_layout(
    title="Heated materials",
    xaxis_title="Youngs Modulus log(MPA)",
)

fig.show()



