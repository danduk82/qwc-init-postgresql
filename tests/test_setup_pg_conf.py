# import test modules
import pytest
import os

# Test the creation of PgServices class
from pgstuff import PgService, PgServices

# test PgService
def test_PgService():
    service = PgService(
        name = "test",
        host = "host",
        port = "port",
        dbname = "dbname",
        user = "user",
        password = "password",
        sslmode = "prefer"
    )
    assert service.name == "test"
    assert service.host == "host"
    assert service.port == "port"
    assert service.dbname == "dbname"
    assert service.user == "user"
    assert service.password == "password"
    assert service.sslmode == "prefer"
    assert str(service) == """[test]
host=host
port=port
dbname=dbname
user=user
password=password
sslmode=prefer
"""
    assert repr(service) == """[test]
host=host
port=port
dbname=dbname
user=user
password=password
sslmode=prefer
"""

# test PgServices
def test_PgServices():
    services = PgServices("pg_service.conf")
    assert services.pg_service_file == "pg_service.conf"
    assert services.services == []
    services.addService(PgService(
        name = "test",
        host = "host",
        port = "port",
        dbname = "dbname",
        user = "user",
        password = "password",
        sslmode = "prefer"
    ))
    assert services.services[0].name == "test"
    assert services.services[0].host == "host"
    assert services.services[0].port == "port"
    assert services.services[0].dbname == "dbname"
    assert services.services[0].user == "user"
    assert services.services[0].password == "password"
    assert services.services[0].sslmode == "prefer"
    assert str(services.services[0]) == """[test]
host=host
port=port
dbname=dbname
user=user
password=password
sslmode=prefer
"""

# test PgServices.getServicesFromEnv
def test_PgServices_getServicesFromEnv():
    services = PgServices("pg_service.conf")
    os.environ["PG_SERVICES_LIST"] = "test"
    os.environ["PG_SERVICE_SERVICENAME_TEST"] = "test"
    os.environ["PG_SERVICE_HOST_TEST"] = "host"
    os.environ["PG_SERVICE_PORT_TEST"] = "port"
    os.environ["PG_SERVICE_DBNAME_TEST"] = "dbname"
    os.environ["PG_SERVICE_USER_TEST"] = "user"
    os.environ["PG_SERVICE_PASSWORD_TEST"] = "password"
    os.environ["PG_SERVICE_SSLMODE_TEST"] = "prefer"
    services.getServicesFromEnv()
    assert services.services[0].name == "test"
    assert services.services[0].host == "host"
    assert services.services[0].port == "port"
    assert services.services[0].dbname == "dbname"
    assert services.services[0].user == "user"
    assert services.services[0].password == "password"
    assert services.services[0].sslmode == "prefer"
    assert str(services.services[0]) == """[test]
host=host
port=port
dbname=dbname
user=user
password=password
sslmode=prefer
"""

