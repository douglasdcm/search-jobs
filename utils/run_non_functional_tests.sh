coverage run --include='app.py' --include='cli.py' --source='src' -m pytest -vvv -s
coverage report
coverage html
