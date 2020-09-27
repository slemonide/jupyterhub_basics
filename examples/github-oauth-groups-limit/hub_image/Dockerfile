FROM jupyterhub/jupyterhub:master

# Need git to get oauthenticator python package directly from git
RUN apt-get update  \
 && apt-get install -yq --no-install-recommends git \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install --no-cache -r /tmp/requirements.txt
COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py
