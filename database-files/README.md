# `database-files` Folder

TODO: Put some notes here about how this works.  include how to re-bootstrap the db. 

The docker compose YAML runs the sql files when it is first run.

When databases are updated, stop and remove the container:
    docker-compose down -v
Then, recreate the container:
    docker-compose up -d
For the changes to take effect.