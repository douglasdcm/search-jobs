coverage run --include='app.py' --include='cli.py' --source='src' -m pytest -vvv -s -m "functional"
coverage report
coverage html
