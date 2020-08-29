FROM pangeo/base-image:master

USER ${NB_USER}

RUN mkdir -p ${HOME}/e350_notebooks

COPY notebooks ${HOME}/e350_notebooks/

WORKDIR ${HOME}/e350_notebooks

CMD ["jupyterhub-singleuser"]
