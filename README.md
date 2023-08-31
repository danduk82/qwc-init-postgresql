# QWC INIT POSTRGRESQL

This repository includes a set of utilities to bootstrap [QWC Services](https://github.com/qwc-services) postgresql dependencies in a kubernetes environment.

## Build the image

```bash
# build the container
export IMAGE_name=your-user/image-name
export IMAGE_TAG=some-tag
make build

# push the image
make push
```

## Generate a pg_services.conf file

To generate a service file:

- the variable `PG_SERVICES_LIST` must be defined, and contain a `,` separated list without white-spaces
- for each profile in the list, the following env variables must be defined:

```bash
# replace <profile-name> with the profile name IN UPPERCASE
PG_SERVICE_HOST_<profile-name>
PG_SERVICE_PORT_<profile-name>
PG_SERVICE_DBNAME_<profile-name>
PG_SERVICE_USER_<profile-name>
PG_SERVICE_PASSWORD_<profile-name>
PG_SERVICE_SSLMODE_<profile-name>
```

you can then run the image

```bash
export IMAGE_NAME=your-user/image-name
export IMAGE_TAG=some-tag

tmpfile=$(mktemp)

cat > $tmpfile << EOF
PG_SERVICES_LIST=profile_a,profile_b

PG_SERVICE_HOST_PROFILE_A=localhost
PG_SERVICE_PORT_PROFILE_A=5432
PG_SERVICE_DBNAME_PROFILE_A=db_a
PG_SERVICE_USER_PROFILE_A=first_user
PG_SERVICE_PASSWORD_PROFILE_A=some_secure_password
PG_SERVICE_SSLMODE_PROFILE_A=require
PG_SERVICE_HOST_PROFILE_B=localhost
PG_SERVICE_PORT_PROFILE_B=5432
PG_SERVICE_DBNAME_PROFILE_B=db_b
PG_SERVICE_USER_PROFILE_B=second_user
PG_SERVICE_PASSWORD_PROFILE_B=some_other_password
PG_SERVICE_SSLMODE_PROFILE_B=prefer
EOF

docker run --rm --env-file $tmpfile -v ${PWD}:${PWD} ${IMAGE_NAME}:${IMAGE_TAG} create-pg-services -f ${PWD}/pg_services.conf

```
