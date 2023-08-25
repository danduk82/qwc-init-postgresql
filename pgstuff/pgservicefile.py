#!/bin/env python

import os
import argparse as ap

# Class PgService
# this class represents a single profile within the pg_service.conf file
class PgService:
 
    pg_service_template = """[%(name)s]
host=%(host)s
port=%(port)s
dbname=%(dbname)s
user=%(user)s
password=%(password)s
sslmode=%(sslmode)s
"""
    def __init__(self, name, host, port, dbname, user, password, sslmode="prefer"):
        self.name = name
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password
        self.sslmode = sslmode
    def __str__(self):
        return self.pg_service_template % self.__dict__
    def __repr__(self):
        return self.__str__()
    
    
# Class PgServices
# This class is used to setup the pg_service.conf file
class PgServices:
    
    def __init__(self, pg_service_file: str):
        self.pg_service_file = pg_service_file
        self.services = []
        
    def addService(self, service: PgService):
        self.services.append(service)
        
    def getServicesFromEnv(self):
        servicesList = os.environ.get("PG_SERVICES_LIST").split(",")
        for serviceName in servicesList:
            service = PgService(
                name = serviceName,
                host = os.environ.get("PG_SERVICE_HOST_" + serviceName.upper()),
                port = os.environ.get("PG_SERVICE_PORT_" + serviceName.upper()),
                dbname = os.environ.get("PG_SERVICE_DBNAME_" + serviceName.upper()),
                user = os.environ.get("PG_SERVICE_USER_" + serviceName.upper()),
                password = os.environ.get("PG_SERVICE_PASSWORD_" + serviceName.upper()),
                sslmode = os.environ.get("PG_SERVICE_SSLMODE_" + serviceName.upper())
            )
            self.addService(service)

    def retriveService(self, name: str):
        for service in self.services:
            if service.name == name:
                return service
        return None
    
    def removeService(self, name: str):
        for service in self.services:
            if service.name == name:
                self.services.remove(service)
                return True
        return False
    
    def __str__(self):
        return "".join([str(service) for service in self.services])
    
    def __repr__(self):
        return self.__str__()
    
    def write(self):
        with open(self.pg_service_file, "w") as f:
            f.write(str(self))
            

# main
if __name__ == "__main__":
    argParser = ap.ArgumentParser(description="Setup pg_service.conf file")
    argParser.add_argument("-f", "--pg-service-file",
                           dest="pg_service_file",
                           default=os.environ.get("PGSERVICEFILE", "/etc/pg_service.conf"),
                           help="Path to pg_service.conf file, derault is {}".format(os.environ.get("PGSERVICEFILE", "/etc/pg_service.conf"))
                           )
    args = argParser.parse_args()
    
    pg_service_file = args.pg_service_file
    services = PgServices(pg_service_file)
    services.getServicesFromEnv()
    services.write()
    
