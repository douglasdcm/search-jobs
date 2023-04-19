coverage run --include='app.py' --include='cli.py' --source='src' -m pytest -vvv -s -m "not performance and not robustness"
coverage report
coverage html
