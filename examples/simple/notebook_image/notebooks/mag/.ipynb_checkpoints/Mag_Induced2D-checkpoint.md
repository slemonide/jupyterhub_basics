---
anaconda-cloud: {}
extensions:
  jupyter_dashboards:
    activeView: report_default
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
    2c77e5c891dd44069234331d87475ef2:
      views:
      - cell_index: 5
  version: 1.2.0
---

+++ {"extensions": {"jupyter_dashboards": {"version": 1, "views": {"grid_default": {"col": 0, "height": 11, "hidden": false, "row": 0, "width": 12}, "report_default": {"hidden": false}}}}}

This is the <a href="https://jupyter.org/">Jupyter Notebook</a>, an interactive coding and computation environment. For this lab, you do not have to write any code, you will only be running it. 

To use the notebook:
- "Shift + Enter" runs the code within the cell (so does the forward arrow button near the top of the document)
- You can alter variables and re-run cells
- If you want to start with a clean slate, restart the Kernel either by going to the top, clicking on Kernel: Restart, or by "esc + 00" (if you do this, you will need to re-run the following block of code before running any other cells in the notebook) 

This notebook uses code adapted from 

SimPEG
- Cockett, R., S. Kang, L.J. Heagy, A. Pidlisecky, D.W. Oldenburg (2015, in review), SimPEG: An open source framework for simulation and gradient based parameter estimation in geophysical applications. Computers and Geosciences

```{code-cell} ipython3
---
extensions:
  jupyter_dashboards:
    version: 1
    views:
      grid_default:
        col: 0
        height: 3
        hidden: true
        row: 11
        width: 12
      report_default:
        hidden: true
---
import numpy as np
from geoscilabs.mag import Mag, Simulator
from SimPEG import PF, Utils, Mesh
%matplotlib inline
```

+++ {"extensions": {"jupyter_dashboards": {"version": 1, "views": {"grid_default": {"col": 0, "height": 21, "hidden": false, "row": 22, "width": null}, "report_default": {"hidden": false}}}}}

# How do we define direction of an earth magnetic field?

Earth magnetic field is a vector. To define a vector we need to choose a coordinate system. We use right-handed system: 
- X (Easting), 
- Y (Northing), and 
- Z (Up). 

Here we consider an earth magnetic field ($\vec{B_0}$), of which intensity is one. To define this unit vector, we use inclinatino and declination:
- Declination: An angle from geographic North (Ng) (positive clockwise)
- Inclination: Vertical angle from the N-E plane (positive down)

<img src="https://github.com/geoscixyz/geosci-labs/raw/master/images/mag/earthfield.png?raw=true" style="width: 60%; height: 60%"> </img>

+++ {"extensions": {"jupyter_dashboards": {"version": 1, "views": {"grid_default": {"col": 0, "height": 18, "hidden": false, "row": 43, "width": null}, "report_default": {"hidden": false}}}}}

# What's data: total field anomaly

We consider a typical form of magnetic data. To illustrate this we consider an suceptible object embedded in the earth. 
Based upon the earth magnetic field ($\vec{B}_0$), this object will generate anomalous magnetic field ($\vec{B}_A$). We define an unit vector $\hat{B}_0$ for the earth field as 
$$ \hat{B}_0 = \frac{\vec{B}_0}{|\vec{B}_0|}$$ 
We measure both earth and anomalous magnetic field such that

$$ \vec{B} = \vec{B}_0 + \vec{B}_A$$

Total field anomaly, $\triangle \vec{B}$ can be defined as

$$  |\triangle \vec{B}| = |\vec{B}|-|\vec{B}_E| $$ 

If $|\vec{B}|\ll|\vec{B}_E|$, then that is total field anomaly $\triangle \vec{B}$ is the projection of the anomalous field onto the direction of the earth field:

$$ |\triangle \vec{B}| \simeq \vec{B}_A \cdot \hat{B}_0=|\vec{B}_A|cos\theta$$ 

<img src="https://github.com/geoscixyz/geosci-labs/raw/master/images/mag/totalfieldanomaly.png?raw=true" style="width: 50%; height: 50%">

+++ {"extensions": {"jupyter_dashboards": {"version": 1, "views": {"grid_default": {"col": 0, "height": 11, "hidden": false, "row": 11, "width": 6}, "report_default": {"hidden": false}}}}}

# Define a 3D prism
Our model is a rectangular prism. Parameters to define this prism are given below:

- dx: length in Easting (x) direction (meter)
- dy: length in Northing (y) direction (meter)
- dz: length in Depth (z) direction (meter) below the receiver
- depth: top boundary of the prism (meter)
- pinc: inclination of the prism (reference is a unit northing vector; degree)
- pdec: declination of the prism (reference is a unit northing vector; degree)

You can also change the height of the survey grid above the ground
- rx_h: height of the grid (meter)

*Green dots show a plane where we measure data.*

```{code-cell} ipython3
---
extensions:
  jupyter_dashboards:
    version: 1
    views:
      grid_default:
        col: 0
        height: 28
        hidden: false
        row: 61
        width: 6
      report_default:
        hidden: true
---
#Input parameters
fileName = 'https://github.com/geoscixyz/geosci-labs/raw/master/assets/mag/data/DO27_TMI.dat'
xyzd = np.genfromtxt(fileName, skip_header=3)
B = np.r_[60308, 83.8, 25.4]
survey = Mag.createMagSurvey(xyzd, B)
# View the data and chose a profile
param = Simulator.ViewMagSurvey2D(survey)
display(param)
```

```{code-cell} ipython3
param.result
```

```{code-cell} ipython3
# Define the parametric model interactively
model = Simulator.ViewPrism(param.result)
display(model)
```

+++ {"extensions": {"jupyter_dashboards": {"version": 1, "views": {"grid_default": {"col": 6, "height": 11, "hidden": false, "row": 11, "width": 6}, "report_default": {"hidden": false}}}}}

# Magnetic applet
Based on the prism that you made above, below Magnetic applet computes magnetic field at receiver locations, and provide both 2D map (left) and profile line (right). 

For the prism, you can alter:
- sus: susceptibility of the prism

Parameters for the earth field are:
- Einc: inclination of the earth field (degree)
- Edec: declination of the earth field (degree)
- Bigrf: intensity of the earth field (nT)

For data, you can view:
- tf: total field anomaly,  
- bx :x-component, 
- by :y-component, 
- bz :z-component

You can simulate and view remanent magnetization effect with parameters:
- irt: "induced", "remanent", or "total"
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
        height: 28
        hidden: false
        row: 61
        width: 6
      report_default:
        hidden: true
---
plotwidget = Simulator.PFSimulator(model, param)
display(plotwidget)
```

```{code-cell} ipython3

```
