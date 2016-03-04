#!/bin/bash
sudo pg_restore --disable-triggers --data-only [dump_banco.tar] | docker exec -i sapl_db_1 psql -U postgres
