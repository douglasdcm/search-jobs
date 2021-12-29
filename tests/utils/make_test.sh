
# disable the real crawlers for test and development
echo "Changing source code to be developed."
sed -i 's/\"enabled\": True/\"enabled\": False/' src/crawler/factory.py
# ensure the database is postgres
sed -i 's/DB_TYPE = {\"p\": \"postgres\"/DB_TYPE = {\"p\": \"sqlite\"/' src/settings.py
echo "Code ready to be developed."