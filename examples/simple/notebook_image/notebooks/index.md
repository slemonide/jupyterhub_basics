---
anaconda-cloud: {}
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
---

# GPG Labs

<a href="http://gpg.geosci.xyz"><img src="http://gpg.geosci.xyz/_images/intro.png" alt="http://gpg.geosci.xyz" align="right" width="200"></a>

This collection of notebooks covers basic principles of applied geophysics. Associated material can be found in the <a href="http://gpg.geosci.xyz">GPG: Geophysics for Practicing Geoscientists</a>.



If you have feedback, we would like to hear from you! 
- <a href="http://slack.geosci.xyz/">Contact us</a>
- <a href="https://github.com/ubcgif/gpgLabs/issues">Report issues</a>
- <a href="https://github.com/ubcgif/gpgLabs/">Join the development</a>

+++

## Contents

### Magnetics
- [MagneticDipoleApplet.ipynb](mag/MagneticDipoleApplet.ipynb) - Magnetic dipole applet
- [MagneticPrismApplet.ipynb](mag/MagneticPrismApplet.ipynb) - Magnetic prism applet
- [Mag_Induced2D.ipynb](mag/Mag_Induced2D.ipynb)- Induced magnetic anomaly demo
- [Mag_FitProfile.ipynb](mag/Mag_FitProfile.ipynb)- Fit one magnetic profile from field observation

### Seismic
- [SeismicApplet.ipynb](seismic/SeismicApplet.ipynb) - Seismic Applet
- [Seis_Refraction.ipynb](seismic/Seis_Refraction.ipynb) - Seismic refraction survey demo
- [Seis_Reflection.ipynb](seismic/Seis_Reflection.ipynb) - Synthetic reflection seismogram
- [Seis_NMO.ipynb](seismic/Seis_NMO.ipynb) - Normal moveout demo
- [Seis_VerticalResolution.ipynb](seismic/Seis_VerticalResolution.ipynb) - Vertical resolution in reflection

### Ground Penetrating Radar
- [GPR_TBL4_DOI_Resolution.ipynb](gpr/GPR_TBL4_DOI_Resolution.ipynb) - Horizontal resolution + Probing distance of GPR
- [GPR_Lab6_FitData.ipynb](gpr/GPR_Lab6_FitData.ipynb) - Fit field GPR data
- [GPR_Attenuation.ipynb](gpr/GPR_Attenuation.ipynb) - Explore the impact of electrical conductivity on attenuation of signals

### Electromagnetics
- [InductionRLcircuit_Harmonic.ipynb](em/InductionRLcircuit_Harmonic.ipynb) - Two coil app
- [FDEM_ThreeLoopModel.ipynb](em/FDEM_ThreeLoopModel.ipynb) - EM induction explained by a 3-loop circuit model
- [EM_Pipeline.ipynb](em/EM_Pipeline.ipynb) - EM response over a pipeline
- [EM_EM31.ipynb](em/EM_EM31.ipynb) - EM-31 response and apparent conductivity

### Direct Current Resistivity
- [DC_SurveyDataInversion.ipynb](dcip/DC_SurveyDataInversion.ipynb) - Physics, survey, data and interpretation

+++

<center><a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" width=60 src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a> 

This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.</center>

```{code-cell} ipython3
# !pip install -r ../requirements.txt
```
