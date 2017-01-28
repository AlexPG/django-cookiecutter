# Django-cookiecutter
A simple cookiecutter to start easily your django projects.

# Requirements
+ Python 3.4
+ Virtualenv

# Installation
Download the repo in your target directory and unzip it. Create a virtualenv and activate it.

Then you have to install cookiecutter.

```python
pip install cookiecutter
```

After that you have to run cookiecutter against the repo.
```python
cookiecutter repo_name
```
You will be asked about the project name and packages to install.

Once is finished move to the newly created directory. Inside requirements folder you can install base, local, test or all packages with
```python
pip install -r requirements_file.txt
```

Finally, after running your project, you have to set SYSTEM_ENV variable to local, test or production. Once is set, if no matches are found the default is local.
```python
export SYSTEM_ENV=local|test|production
```
# Usage
Type
```python
pyhton manage.py runserver
```
 and you will run the development server.

Now you can navigate to [localhost:8000](http://localhost:8000).