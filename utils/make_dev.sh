
echo "Changing source code to be developed."
sed -i 's/https:\/\/vagaspramim\.herokuapp\.com/http:\/\/localhost:5000/' templates/index.html
sed -i 's/\"enabled\": True/\"enabled\": False/' src/crawler/factory.py