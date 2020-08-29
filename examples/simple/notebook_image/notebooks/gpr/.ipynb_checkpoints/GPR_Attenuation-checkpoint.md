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
widgets:
  state:
    234b50583b3246edb24ab70aee35c4e4:
      views:
      - cell_index: 5
  version: 1.2.0
---

```{code-cell} ipython3
%matplotlib inline
from geoscilabs.gpr.Attenuation import AttenuationWidgetTBL
```

# Attenuation of EM wave

+++

To simplify the GPR problem, we assumed that we do not have conductivity effect. However, in practice, this is not true. For instance, the earth medium can have considerably high conductivity values. In this case, EM wave attenuates as a function of conductivity ($\sigma$), permittivity ($\epsilon$), and frequency ($f$). Thus, we can write velocity of EM wave as:

$$ v(\sigma, f, \epsilon)$$

In addition, electromagnetic wave, which propagates in the earth attenuates in several reasons why:

- Geometric decaying
- Electrical conductivity ($\sigma$, S/m)

To measure how much it attenuates we define skin depth as the depth at which the intensity of the radiation inside the material falls to 1/e (about 37%) of its original value. And it can be written as:

$$ \delta(\sigma, f, \epsilon) $$

By adjusting parameters below, you will indentify how velocity and skin depth change as a function of $\sigma$, $\epsilon$, and $f$.

+++

## Parameters:

+++

- $\epsilon_r$: Relative permittivity of the medium

- $log(\sigma)$: Log10(Conductivity, S/m)

- $log(f)$: Log10(frequency, Hz)

```{code-cell} ipython3
AttenuationWidgetTBL()
```

```{code-cell} ipython3

```
