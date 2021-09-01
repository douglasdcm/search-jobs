
sed -i 's/http:\/\/localhost:5000/https:\/\/vagaspramim\.herokuapp\.com/' templates/index.html
git status
git add .
git commit -m "Release new version of the app"
git push origin master
sed -i 's/https:\/\/vagaspramim\.herokuapp\.com/http:\/\/localhost:5000/' templates/index.html
 