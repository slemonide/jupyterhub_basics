FROM phaustin/base-image:sep05

USER ${NB_USER}

RUN mkdir -p ${HOME}/notebooks

COPY notebooks ${HOME}/notebooks/

WORKDIR ${HOME}

CMD ["jupyterhub-singleuser"]
