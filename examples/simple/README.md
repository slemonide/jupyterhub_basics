
Original source:  https://github.com/jupyterhub/dockerspawner/tree/master/examples/simple


# Running JupyterHub itself in docker

This is a simple example of running jupyterhub in a docker container.

This example will:

- create a docker network
- run jupyterhub in a container
- enable 'dummy authenticator' for testing
- run users in their own containers

It does not:

- enable persistent storage for users or the hub
- run the proxy in its own container

```
cd jupyterhub_basics/examples/simple
./bringdown.sh
docker-compose pull notebook
docker-compose build jupyterhub
docker-compose up
```

Now we should have jupyterhub running on port 8000 on our docker host.

Point a browser at:

```
localhost:8000
```

and log in with any userid and any password.  You should see a jupyterhub splash screen and be able to start a scipy notebook.


## Further goals

This shows the *very basics* of running the Hub in a docker container (mainly setting up the network). To run for real, you will want to:

- mount a volume (or a database) for the hub state
- mount volumes for user storage so they don't lose data on each shutdown
- pick a real authenticator
- run the proxy in a separate container so that reloading hub configuration doesn't disrupt users

[jupyterhub-deploy-docker](https://github.com/jupyterhub/jupyterhub-deploy-docker) does all of these things.
