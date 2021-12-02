
# disable the real crawlers for test and development
echo "Changing source code to be developed."
sed -i 's/\"enabled\": True/\"enabled\": False/' src/crawler/factory.py
echo "Code ready to be developed."