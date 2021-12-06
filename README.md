## Automated ETL

[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)

> "An automated pipeline which works like that --> [E]xtract images locally, [T]ranform them applying a 3D human pose estimation model and [L]oad them (+ more details) into PostgreSQL database."

### Quickstart
Download or clone this [repo.](https://github.com/pan-efs/AutomatedETL_3DHPE)

Install `Docker` on your system, following the [instructions.](https://docs.docker.com/get-docker/)

For formal reasons, the application has been developed in `WSL2 Ubuntu 20.04` and `conda` as package and environment management.

### Step 1: Configuration
Run the bash script `config.sh` parsing the following flags:

```diff
- -u, Define the username for the PostgreSQL DBMS.
- -p, Defind the password for the PostgreSQL DBMS.
- -d, Give a name for the database that would you like to store the data.
- -t, Give a name for the table into the database which has been created using the above flag. 
```

Example, `root$ bash config.sh -u myusername -p mypassword -d mydatabase -t mytable`, where `root` is the path to the repo in your local filesystem.

### Step 2: Build docker locally
#TODO:...