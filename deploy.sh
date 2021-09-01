
sed -i 's/http:\/\/localhost:5000/https:\/\/vagaspramim\.herokuapp\.com/' templates/index.html
sed -i 's/\"enabled\": False/\"enabled\": True/' src/crawler/factory.py
sed -i 's/DEBUG = True\DEBUG = False/' src/settings.py
pip freeze > requirements.txt
git status
git add .
git commit -m "Release new version of the app"
# git push origin master
sed -i 's/https:\/\/vagaspramim\.herokuapp\.com/http:\/\/localhost:5000/' templates/index.html
sed -i 's/\"enabled\": True/\"enabled\": False/' src/crawler/factory.py