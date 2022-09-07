.PHONY: run
run:
		python3 main.py

.PHONY: connectDB
connectDB:
		docker exec -it 72ecabb63e44 /bin/bash

# create database dump file
.PHONY: dump
dump:
		pg_dump -C -h localhost -d postgres -p 58060 -U postgres -W > backup.sql

