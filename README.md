# DATAOX test assignment for junior python developer position

## Zhovtaniuk Maksym

### config.py:
MAX_PAGES - amount of pages to be parsed by the program

### To create database dumpfile:
```commandline
make dump
```
or
```commandline
pg_dump -C -h localhost -d postgres -p 58060 -U postgres -W > backup.sql
```
