FROM phaustin/base-image:sep05

USER ${NB_USER}

RUN mkdir -p ${HOME}/work

WORKDIR ${HOME}/work

CMD ["jupyterhub-singleuser"]
