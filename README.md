# Create Your Own Hierarchical Data

Using Modified Preorder Tree Transversal (MPTT), it's possible to treat the data like a gigantic tree,
with a single starting point (the "root" boject) and parents, siblings, and children galore.

## Installation

1. Use the package manager [poetry](https://python-poetry.org/) to start a virtual environment:

```bash
    poetry shell
```

2. Then, install all the dependencies required for this project:

```bash
    poetry install
```

3. Finally, because all the migrations are already made and the database as well, run the server with the following command:

```bash
    python manage.py runserver
```

## How to start

1. Click [here](http://localhost:8000/signup/) to create a new user or use this command and follow the process:

```bash
    python manage.py createsuperuser
```

2. Then, log in into your account and you can start creating new folders/files for your own tree!
3. Finally, you are optional to create new users and store their own trees base on the user is currently logged in.

## Animals hierarchical data

There is already a user created where you can see the Hierarchical Data of Animals and feel free to play with it.

The username is `apple` and the password is `1234`.

## References

If you want to know more about django-mptt visit this [link](https://django-mptt.readthedocs.io/en/latest/)
