# projeto-inovacao-ifba
## Projeto Inovação 

Components:
1. Felipe
2. Igor
3. Italo
4. Manoel Vitor
5. Matheus
6. Prof. Paulo
7. Sheory

## How to clone This Repository

To clone this repository to your local machine, follow the steps bellow:

1. Open the terminal
2. Navigate to the directory where you want to clone  the repository.
3. Execute command to clone the repository

```bash
cd C:/users/{your_username}/Documents/
git clone https://github.com/pauloperris/projeto-inovacao-ifba.git
cd C:/users/{your_username}/Documents/projeto-inovacao-ifba
```

## How to install dependences
1. Open the terminal
2. Navigate to the directory where are to save the repository.
3. Intro you will to execute  command

```bash
cd C:/users/{your_username}/Documents/projeto-inovacao-ifba
pip install -r requirements.txt
```

## How to fix error with library dlib
1. Open the terminal
2. Navigate to the directory where are to clone the repository.
3. Execute command to install library
```bash
cd C:/users/{your_username}/Documents/projeto-inovacao-ifba
pip install dlib-19.19.0-cp38-cp38-win_amd64.whl
```

## How to create database

1. Open the terminal
2. Execute to command
3. Type to your password

```bash
mysql -u {username} -p
```
Now we will execute query to create the database
```sql
CREATE DATABASE image_db;
```
Now we will execute query to create us the table

```sql
CREATE TABLE image_table(
   id_pessoa INT NOT NULL AUTOINCREMENT,
   nome_pessoa VARCHAR(32) NOT NULL,
   image_pessoa LONGBLOB,
   phone_pessoa VARCHAR(15) NOT NULL,
   email_pessoa VARCHAR(150) NOT NULL,
   PRIMARY KEY(id_pessoa)
);
```

## Please, Look to mysql.py file and writer your credencial to connect database any difficulty.

Example:


```python
# library that you will to use
from dao.mysql import DatabaseConnect
# instance that you will to create.
db = DatabaseConnect(
  "image_db", # Database name
  "root", # User to database
  "root", # Password to database
  "localhost", # host name or IP
  "3306" # port number, by default mysql to use the port 3306
)
```