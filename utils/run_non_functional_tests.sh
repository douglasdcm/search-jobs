coverage run --include='app.py' --include='cli.py' --source='src' -m pytest -vvv -s -m "performance or robustness"
coverage report
coverage html
