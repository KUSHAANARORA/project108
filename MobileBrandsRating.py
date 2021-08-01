import pandas as pd
import plotly.express as py
import plotly.figure_factory as pf
with open ("data.csv") as f:
  s = pd.read_csv(f)
d = pf.create_distplot([s["Avg Rating"].tolist()],["Rating"],show_hist=False)
d.show()