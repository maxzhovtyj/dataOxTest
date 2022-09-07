.PHONY: run
run:
		go run ./cmd/main.go

.PHONY: connectDB
connectDB:
		docker exec -it 72ecabb63e44 /bin/bash

.PHONY: dump
dump:
		pg_dump -C -h localhost -d postgres -p 58060 -U postgres -W > backup.sql

