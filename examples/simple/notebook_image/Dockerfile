FROM pangeo/base-image:master

USER ${NB_USER}

RUN mkdir -p ${HOME}/notebooks

COPY notebooks ${HOME}/notebooks/

WORKDIR ${HOME}

CMD ["jupyterhub-singleuser"]
