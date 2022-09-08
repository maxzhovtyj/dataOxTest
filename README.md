# DATAOX test assignment for junior python developer position

## Zhovtaniuk Maksym

### config.py:
MAX_PAGES - amount of pages to be parsed by the program;  
host - name of host (docker service name of postgres database, change to localhost outside docker);    
port - database port (docker inner port 5432, change to 58068 outside docker);      
user - database username  
password - database user password !BETTER TO SAVE IN .env  

### Build an app and run docker-compose
```commandline
docker-compose up --build app
```

### Build
```commandline
docker build -t app .
```

### Run outside docker
* Change host and port values
* Run docker postgres db 
```commandline
docker run --name=dataOx -e POSTGRES_PASSWORD=qwerty123 -p 58060:5432 -d postgres
```
* Run:
```commandline
python3 main.py
```

### To create database dumpfile:
```commandline
make dump
```
or
```commandline
pg_dump -C -h localhost -d postgres -p 58060 -U postgres -W > backup.sql
```
