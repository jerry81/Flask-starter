# Flask-starter

## getting started

- install venv
```
python3 -m venv venv
```
- note venv is a python thing but it has some integrations with zsh

- activate virtual env
```
source venv/bin/activate
```

- double check that we are using venv's tools
```
which python
```
- this actually is a symlink to python3

- note the previous steps must be run each time a new shell env is created
- it can be automated with a script

- install flask
```
pip install flask
```

- save dependencies
```
pip freeze > requirements.txt
```

## note aboute packages

- jinja for HTML templating