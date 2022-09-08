.PHONY: run
run:
		python3 main.py

# create database dump file
.PHONY: dump
dump:
		pg_dump -C -h localhost -d postgres -p 58060 -U postgres -W > backup.sql

