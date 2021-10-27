
echo "Changing source code to be deployed."
echo "" > ./logs/crawler.log
sed -i 's/\"enabled\": False/\"enabled\": True/' src/crawler/factory.py
sed -i 's/DEBUG \= True/DEBUG \= False/' src/settings.py
pip freeze > requirements.txt
git status

