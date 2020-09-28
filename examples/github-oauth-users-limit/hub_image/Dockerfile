FROM jupyterhub/jupyterhub:master
COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install --no-cache -r /tmp/requirements.txt
COPY userlist /srv/jupyterhub/userlist
COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py
