# building the image for eosc 350

1) build the meta-package with the basic notebook dependencies

```
conda build base_recipe
```

which should upload the package to anaconda in the eoas_ubc channel as base_notebook version 2020.08.24

2) build the conda-lock file

cd notebook_image
conda-lock --file environment.yml -p linux-64


