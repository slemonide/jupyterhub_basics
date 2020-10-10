# dummy for testing. Don't use this in production!
#c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'

# launch with docker
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

# we need the hub to listen on all ips when it is in a container
c.JupyterHub.hub_ip = '0.0.0.0'
# the hostname/ip that should be used to connect to the hub
# this is usually the hub container's name
c.JupyterHub.hub_connect_ip = 'jupyterhub_basic'

# pick a docker image. This should have the same version of jupyterhub
# in it as our Hub.
c.DockerSpawner.image = 'phaustin/notebook:step1'
notebook_dir = "/home/jovyan/work"
c.DockerSpawner.notebook_dir = notebook_dir

# tell the user containers to connect to our docker network
c.DockerSpawner.network_name = 'net_basic'
#  - "/data/jupyterhub_basics/examples/github-oauth/reverse-proxy/usr/share/nginx/html:/usr/share/nginx/html"
#c.DockerSpawner.volumes = {"jupyterhub-user-{username}": notebook_dir}
c.DockerSpawner.volumes = {"/data/jupyterhub/backup/jupyter/jupyterhub-user-{username}/home/jovyan/work": notebook_dir}
# delete containers when the stop
c.DockerSpawner.remove = True

# Create a user directory with correct permissions to make it writable from the juputer
import os
def create_dir_hook(spawner):
    username = spawner.user.name # get the username
    volume_path = '/data/jupyterhub/backup/jupyter/jupyterhub-user-%(username)s/home/jovyan/work' % locals()
    if not os.path.exists(volume_path):
        # create a directory with umask 0755 
        # hub and container user must have the same UID to be writeable
        # still readable by other users on the system
        os.makedirs(volume_path, 0o755)
        os.chown(volume_path, 1000, 1000)

# attach the hook function to the spawner
c.Spawner.pre_spawn_hook = create_dir_hook


# Github OAuth
from oauthenticator.github import GitHubOAuthenticator
c.JupyterHub.authenticator_class = GitHubOAuthenticator
c.GitHubOAuthenticator.allowed_organizations = ['eoas-ubc-github-shared-test']

# Load users from access list
import os

c.Authenticator.whitelist = whitelist = set()
c.Authenticator.admin_users = admin = set()

join = os.path.join
here = os.path.dirname(__file__)
with open(join(here, 'userlist')) as f:
    for line in f:
        if not line:
            continue
        parts = line.split()
        name = parts[0]
        whitelist.add(name)
        if len(parts) > 1 and parts[1] == 'admin':
            admin.add(name)

