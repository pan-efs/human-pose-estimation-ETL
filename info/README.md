### CLI : TROUBLESHOOTING

### Install psycopg2 on WSL2 (Ubuntu 20.04) in a conda environment

- `conda create -n 'env_name' python=3.8.x`
- `conda activate 'env_name'`
- `sudo apt install python3-dev libpq-dev`
- `pip3 install wheel`, if it is not satisfied.
- `pip3 install psycopg2`

### Extract requirements.txt file
The below command concentrates only the packages for the project, yet you have to modify it, i.e. convert `=` symbol to `==`. 
- conda list -e > requirements.txt

### Four useful commands for postgreSQL locally
* sudo service postgresql status
* sudo service postgresql start
* sudo service postgresql stop
* sudo -u postgres psql

### Docker-compose
- docker-compose build
- docker-compose up || docker-compose up -d
- docker-compose down
- docker-compose ps

- docker-compose exec <service> bash
- psql -h <host_db_service> -U <user> -d <database_name>

- `Linux:` sudo ls /mnt/wsl/docker-desktop-data/data/docker/volumes
- `Windows:` \\wsl$\docker-desktop-data\mnt\wsl\docker-desktop-data\data\docker\volumes