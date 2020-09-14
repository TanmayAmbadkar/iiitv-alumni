## Alumni Portal for IIIT Vadodara

This will be the alumni portal for IIIT Vadodara

___
## Setup

```sh
$ git clone https://github.com/TanmayAmbadkar/iiitv-alumni.git
$ cd iiitv-alumni
```

### For setting virtual environment

```sh
$ virtualenv venv
```

### For activating virtual environment in Windows

```sh
$ venv/Scripts/activate
```

### For activating virtual environment in Linux and macOS

```sh
$ source venv/bin/activate
```

### For deactivating virtual environment
```sh
$ deactivate
```
After creating virtual environment

### Start

```sh
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
