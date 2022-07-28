# Mongodb Docker 

If there's any changes in logins or password, or database. Please note that you would need to use the previously specified logins from the previous instance built initially, because the database files are built from the original instance.

Use the cleanup script `clear-db` as root, it will auto clear the /root/docker_instances/mongo folder

Start this instance using the docker-compile script, which is just a shortcut for:

```docker-compse up ```

or run as detached:

```docker-compose up -d```

### ToDo

### Default logins & Testing

- Login as `mongodb_administrator`
- Password as `UiIkM8VKvu5hn1b3KRnnQZvlrMJeaHZt`

You can test using mongodb shell using cmd:

```mongo --host 127.0.0.1 --port 27017 -u mongodb_administrator --shell```

Alternatively you can edit directly because mongo-express can web manage the db directly

[127.0.0.1:8081](127.0.0.1:8081)

Passwords and variables are customizable via env folder's vars file, but must be reflected in also the admin.env because the mongo-express this information to login.
