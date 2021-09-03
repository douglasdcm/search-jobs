
echo "Changing source code to be deployed."
sed -i 's/http:\/\/localhost:5000/https:\/\/vagaspramim\.herokuapp\.com/' templates/index.html
sed -i 's/\"enabled\": False/\"enabled\": True/' src/crawler/factory.py
sed -i 's/DEBUG \= True/DEBUG \= False/' src/settings.py
pip freeze > requirements.txt
git status

