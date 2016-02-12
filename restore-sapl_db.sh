#!/bin/bash
sudo pg_restore --disable-triggers --data-only sapl_12-02-16.tar | docker exec -i sapl_db_1 psql -U postgres