# Trambo -- Final Project - Docker

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


 - First Step
```
    $ docker build -t <name>:<tag> .

    $ docker build -t <name>:<tag> --secret id=db_user,src=./secret_user.txt .
```
 - Second Step
```
    $ docker run -it --rm -p 5000:5000 final:one
```