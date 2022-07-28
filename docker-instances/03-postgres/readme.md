# New Docker using Postgres image

If there's any changes in logins or password, or database. Please note that you would need to use the previously specified logins from the previous instance built initially, because the database files are built from the original instance.

If you don't care about the existing instance's data, you can delete the psql folder within this folder, and rebuild using docker-compile or the command directly

```docker-compse up ```

or run as detached:

```docker-compose up -d```

### ToDo

- ~~Set mounting point~~
- ~~Creating Users~~
- ~~Allow external login~~
- ~~Segregate Execution script to run on dockerfile instead of compose~~
- ~~environmental file to seperate logins~~ 

### Default logins & Testing

- Login as `postgres_user`
- Database as `postgres_database`
- Password as `BasicPassword!`

You can test internally on the server via port as this:

```psql -h 127.0.0.1 -p 45432 -U postgres_user -d postgres_database```
