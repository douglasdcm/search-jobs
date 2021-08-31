# Introduction
This project is intended to use crawlers to search for positions in differet company pages and expose a way to users compare their curiculum against the positions to have a ranking of positions that matches the curriculum.
# Getting started
To run the crawler, just do:
<br><code>python main.py --initdb</code>
<br><code>python main.py --run</code><br><br>
It will run the implemented crawlers, get the desired information from company pages and save it in database.
After that you can compare your curriculum to find the positions that better fits it.
<br><code>python main.py --compare <path/to/file/curriculum.txt></code><br><br>
Try "--help" for more information
<br><code>python main.py --help</code><br>
The curriculum can be compared using the Web page. Just run:
<br><code>python app.py</code><br><br>
and go to http://localhost:5000
# Contributing
If you want to add a new crawler, you need to follow the ICrawler protocol. So, the needed fields must to be saved into database.
Steps to add a new crawler:
- Add the crawler in a new file the crawler directory
- Add this new crawler to factory.py under the commented line

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

Mark the repository with a star if liked it.