---
anaconda-cloud: {}
extensions:
  jupyter_dashboards:
    activeView: grid_default
    version: 1
    views:
      grid_default:
        cellMargin: 10
        defaultCellHeight: 20
        maxColumns: 12
        name: grid
        type: grid
      report_default:
        name: report
        type: report
jupytext:
  cell_metadata_filter: all
  notebook_metadata_filter: all,-toc,-latex_envs
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: 1.4.2
kernelspec:
  display_name: Python 3
  language: python
  name: python3
language_info:
  codemirror_mode:
    name: ipython
    version: 3
  file_extension: .py
  mimetype: text/x-python
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
  version: 3.7.6
widgets:
  state:
    8789ea09a28443d0b196412593e51195:
      views:
      - cell_index: 3
    8bd53575b8d6470cb6158b113159182e:
      views:
      - cell_index: 5
  version: 1.2.0
---

+++ {"extensions": {"jupyter_dashboards": {"version": 1, "views": {"grid_default": {"col": 0, "height": 10, "hidden": false, "row": 0, "width": 12}, "report_default": {"hidden": false}}}}}

This is the <a href="https://jupyter.org/">Jupyter Notebook</a>, an interactive coding and computation environment. For this lab, you do not have to write any code, you will only be running it. 

To use the notebook:
- "Shift + Enter" runs the code within the cell (so does the forward arrow button near the top of the document)
- You can alter variables and re-run cells
- If you want to start with a clean slate, restart the Kernel either by going to the top, clicking on Kernel: Restart, or by "esc + 00" (if you do this, you will need to re-run the following block of code before running any other cells in the notebook) 

This notebook uses code adapted from 

SimPEG
- Cockett, R., S. Kang, L.J. Heagy, A. Pidlisecky, D.W. Oldenburg (2015, in review), SimPEG: An open source framework for simulation and gradient based parameter estimation in geophysical applications. Computers and Geosciences

+++ {"extensions": {"jupyter_dashboards": {"version": 1, "views": {"grid_default": {"col": 0, "height": 11, "hidden": false, "row": 10, "width": 6}, "report_default": {}}}}}

## View the model

- dx: width or prism in x-direction (m)
- dy: width of prism in y-direction (m)
- dz: vertical extent of prism (m)
- x0: x location of the center of the prism (m)
- y0: y location of the center of the prism (m)
- depth: depth to the top of the prism (m)
- prism_inc: inclination of the prism (reference is a unit northing vector; degrees)
- prism_dec: declination of the prism (reference is a unit northing vector; degrees)
- View_dip: dip angle of view (degrees)
- View_elev: elevation of view (degrees)
- View_azim: azimuth of view (degrees)

```{code-cell} ipython3
---
extensions:
  jupyter_dashboards:
    version: 1
    views:
      grid_default:
        col: 0
        height: 29
        hidden: false
        row: 21
        width: 6
      report_default:
        hidden: false
---
import numpy as np
from geoscilabs.mag import Mag, Simulator
from SimPEG import PF, Utils, Mesh
from ipywidgets import widgets
import matplotlib
%matplotlib inline
```

```{code-cell} ipython3
#Input parameters
fileName = 'http://github.com/geoscixyz/geosci-labs/raw/master/assets/mag/data/Lab1_Wednesday_TA.csv'
data = np.genfromtxt(fileName, skip_header=1, delimiter=',')
xyzd = np.c_[np.zeros(data.shape[0]), data[:,0], np.zeros(data.shape[0]), data[:,1]]
B = np.r_[60308, 83.8, 25.4]
survey = Mag.createMagSurvey(xyzd, B)
# View the data and chose a profile
# Define the parametric model interactively
model = Simulator.ViewPrism(survey)
display(model)
```

## Fit the data
- Binc: Inclination of the Earth's background field (degree)
- Bdec: Declination of the Earth's background field (degree)
- Bigrf: Strength of the Earth's background field (nT) 
- depth: vertical distance from the sensor to the top of the rebar (m)
- susc: magnetic susceptibility
- comp: Total field (tf) of component of the field to plot
- irt: Type of magnetization 
- Q: Koenigsberger ratio ($\frac{M_{rem}}{M_{ind}}$)
- rinc: inclination of the remanent magnetization (degree)
- rdec: declination of the remanent magnetization (degree)

```{code-cell} ipython3
---
extensions:
  jupyter_dashboards:
    version: 1
    views:
      grid_default:
        col: 6
        height: 29
        hidden: false
        row: 21
        width: 6
      report_default:
        hidden: false
---
Q = Simulator.fitline(model,survey)
display(Q)
```

```{code-cell} ipython3

```

```{code-cell} ipython3

```
