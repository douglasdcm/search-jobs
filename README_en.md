# Introduction
This project is intended to use crawlers to search for positions in different company pages and expose a way to people compare their curriculum vitae (CV) against the positions to have a ranking of positions that matches the curriculum.
# Getting started
To use the crawler just copy the content of your CV in a text file e.g. "/tmp/cv.py", clone this repository, go to its root folder and run:
<br><code>$pip install -r requirements.txt</code>
<br><code>$python main.py --compare /tmp/cv.py</code><br><br>
It will run the implemented crawlers, get the desired information from company pages and save it in database.
After that you can compare your curriculum to find the positions that better fits it.
<br><code>$python main.py --compare /tmp/cv.txt</code><br><br>
A list of similar positions will be printed. The project already has more than 250 positions in database.

Try "--help" for more information
<br><code>$python main.py --help</code><br>
The curriculum can be compared using the Web page. Just run:
<br><code>python app.py</code><br><br>
and go to http://localhost:5000
<br><br>
![alt text](https://i.ibb.co/HH2cJZk/web-page.png)
# Make your own crawlers
It is very easy and simple. In a few minutes you can have your new crawler. You need to follow the "src/crawler/ICrawler.py::Crawler" protocol. So, the needed fields must to be saved into database.
Steps to add a new crawler:
- Add the crawler in a new file in "src/crawler" directory
- Add the Pages Objects for this crawler in the folder "src/pages". Example, "scr/pages/my_crawler/vagas.py"
- Edit the new crawler to use the Page Objects
- Add this new crawler dict to "src/crawler/factory.py" under the commented line
- Add the url of the positions of the company in "src/settings.py::URLS"
- Run:
<br><code>$python main.py --run</code><br><br>
The "enabled" crawlers will be executed and the data will be saved in the database. After that the CV can be compared again.<br><br>
Try "--help" for more information.
<br><code>$python main.py --help</code><br>
# Web page
The curriculum can be compared using the Web page. Run:
<br><code>$python app.py</code><br><br>
and go to http://localhost:5000
<br><br>
![alt text](https://i.ibb.co/HH2cJZk/web-page.png)
# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

Mark the repository with a star if liked it :)