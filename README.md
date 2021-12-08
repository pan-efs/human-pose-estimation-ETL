## Automated ETL Tool

[![AUR maintainer](https://img.shields.io/badge/Houba-Hej%2C%20Folks!-brightgreen)]()
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Github All Releases](https://img.shields.io/github/downloads/pan-efs/AutomatedETL_3DHPE/total.svg)]()

> <img src="info/logo.png" height=150 width=512> "An automated pipeline tool which works like that --> [E]xtract images locally, [T]ranform them applying a 3D human pose estimation model and [L]oad them (+ more details) into PostgreSQL database."

### Quickstart
Download or clone this [repo.](https://github.com/pan-efs/AutomatedETL_3DHPE)

Install `Docker` on your system, following the [instructions.](https://docs.docker.com/get-docker/)

For formal reasons, the application has been developed in `WSL2 Ubuntu 20.04` and `conda` as package and environment management.

### Step 1: Configuration
Run the script `config.sh` parsing the following flags:

```diff
- -u, Define the username for the PostgreSQL DBMS.
- -p, Define the password for the PostgreSQL DBMS.
- -d, Give a name for the database that would you like to store the data.
- -t, Give a name for the table into the database which has been created using the above flag. 
```

For example, `root$ bash config.sh -u myusername -p mypassword -d mydatabase -t mytable`, where `root` is the path to the repo in your local filesystem.

After configuration three new files (db_config.ini, POSTGRES_USER.txt & POSTGRES_PASSWORD.txt) will appear in your filesystem. It's recommended to keep secret those files due to sensitive information. 

### Step 2: Docker-compose Build/Up Locally
Run the script `buildup.sh` parsing the following arguments:

```diff
+ -b, yes/YES, if you want to build the images, otherwise no/NO.
+ -u, yes/YES, if you want to start running the docker containers in the background after building, otherwise no/NO.
```

For instance, the command `root$ bash buildup.sh -b yes -u yes` will build the docker images and then will start running the containers in the background and leaves them running.

See a synopsis of useful docker-compose commands [here.](https://github.com/pan-efs/AutomatedETL_3DHPE/tree/master/info)

### How it works?
#TODO:...