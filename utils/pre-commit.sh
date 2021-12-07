echo "Preparing the project to be pushed to remote repository"
# update requirements
pip freeze > requirements.txt
# report the status of git
git status
# disable the real crawlers for test
sed -i 's/\"enabled\": True/\"enabled\": False/' src/crawler/factory.py
# ensure the database is postgres
sed -i 's/DB_TYPE = {\"p\": \"sqlite\"/DB_TYPE = {\"p\": \"postgres\"/' src/settings.py
# execute the validatation
coverage run --include='app.py' --include='main.py' --source='src' -m pytest -vvv -s -m "not performance"
coverage report
coverage html
# clean the logs
echo "" > ./logs/crawler.log
# enable the real crawlers
sed -i 's/\"enabled\": False/\"enabled\": True/' src/crawler/factory.py
# turn-off the debug mode
sed -i 's/DEBUG \= True/DEBUG \= False/' src/settings.py
echo "Pre-commit finished"

