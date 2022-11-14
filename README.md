## GUIDE

### Install local
```
make install-local
make run
```

Go to `localhost:8000/docs` to view swagger page

### Build image docker
1. Build base image
```
cd ./base-image
make build
# push image to docker hub
make push
```

2. Build the application image
```
make dc-up
```
Go to `localhost:3333/docs` to view swagger page