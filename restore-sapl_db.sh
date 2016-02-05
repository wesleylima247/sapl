#!/bin/bash
pg_restore sapl_03-02-16.tar | docker exec -i sapl_db_1 psql -U postgres
pg_restore sapl_03-02-16.tar | docker exec -i sapl_db_1 psql -U postgres
pg_restore sapl_03-02-16.tar | docker exec -i sapl_db_1 psql -U postgres
pg_restore sapl_03-02-16.tar | docker exec -i sapl_db_1 psql -U postgres