# Definition of some instructions of Docker-Compose file 

```
    build: 
```
* Specifies the directory which contains the Dockerfile containing the instructions for building this service

```
    links:
```
* links this service to another container. This will also allow us to use the name of the service instead of having to find the ip of the database container and express a dependency which will determine the order of start up of the container.

```
    ports:
```
* mapping of <Host>:<Container> ports.


# Summary about Dockerfile app

Set a ENV variable in local terminal for a docker experimental feautures

```
    $ export DOCKER_BUILDKIT=1
```

Add ENV var to Dockerfile

```
    FLASK_ENV: development
    FLASK_APP: app.py
    FLASK_RUN_HOST: 0.0.0.0
```

For run dockerfile with flask aplication

```
    $ docker build -t <name>:<tag> --secret id=db_user,src=./secret_user.txt .
```