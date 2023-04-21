coverage run --source='src' -m pytest -vvv -s -m "functional"
coverage report
coverage html
