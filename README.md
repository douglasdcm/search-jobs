# Introduction
This project is intended to use crawlers to search for positions in differet company pages and expose a way to users compare their curiculum against the positions to have a ranking of positions that matches the curriculum.
# Getting started
To run the crawler, just do:
<br><code>python main.py --run</code><br><br>
It will run the implemented crawlers, get the desired information from company pages and save it in database.
After that you can compare your curriculum to find the positions that better fits it.
<br><code>python main.py --compare <path/to/file/curriculum.txt></code><br><br>
Try "--help" for more information
<br><code>python main.py --help</code><br>
# Contributing
If you want to add a new crawler, you need to follow the ICrawler protocol. So, the needed fields must to be saved into database. See the daitan.py::Daitan class for an example.
Steps to add a new crawler:
- Add the crawler in a new file the crawler directory
- Add this new crawler to main.py under the commented line