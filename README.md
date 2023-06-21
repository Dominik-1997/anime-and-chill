# ANIME & CHILL
#### Video Demo:  https://youtu.be/hecQkkVRAXQ

#### Description:

From the beginning, I have wanted to create something useful to me. And since my friends and I have always spent hours pondering what to watch I decided to make a tool that will ease this process using **Python** since this is the language I am the most proficient at.

Since we are avid fans of Japanese animation, I have chosen to make a web app that will
enable us to browse through the best animes, sort them by tags, and most importantly: show us shows which none of us have not seen already.

Luckily, there already exist two popular websites which allow users to make lists of animes they have seen, want to watch etc, namely: anime-planet.com and myanimelist.net. At first, I decided to use the latter, despite the fact that none of my friends used it. The reason being: bigger possibility of existing official API. However, after a few days of researching old forums I have learned that: there are five or so unofficial APIs, one official obsolete API, one official API in beta, and most importantly, I have learned that API verification process for this page is convoluted so users might
have a hard time getting verified and consequently, being unable to use my webapp.

The other page, anime-planet.com, did not have an official API but the website itself was more transparent and user-friendly, and so, I resorted to web-scraping.

Firstly, I had to somehow download an anime database, titles, ratings, number of episodes, tags, etc. Sadly, I was unable to scrape needed info from the browse-all mode but I noticed that it worked from the "watched" list. So to add all 20 thousand animes to my personal watched list and not lose time (and mind) I had to construct a bot, I decided to use **Selenium**. The process was pretty straightforward and after one tutorial I had a functioning bot.  One of the difficulties I had involved being blocked after making too many requests, too fast and receiving error 503. Luckily, some wait and proper headers solved the issue. The only thing left was to wait. The wait took aprox. 90 minutes, each page had to be fully loaded, then the bot had to do its work and I gave each page a spare 4 seconds to process everything.

The results can be seen on this page:
https://www.anime-planet.com/users/MaxLifeOnAnime
Interestingly, anime-planet calculates how much time one ~~wasted~~ spent on watching anime, and this account is a little short of 9 years of constantly watching anime.

The only thing left to do was to parse the html of each page using **BeautifulSoup4** (in one of the versions I also aided myself with **RegEx**) and write it to the **CSV** file. Luckily, the similar process could be used to get individual users’ lists.

After linking everything together, I had an app counting which anime was seen by inputted users, no apis, no verification.

The only thing left to do was to make a website, I used **html**, **Bootstrap**, a little bit of **JavaScript**, and **Jinja**.
After the page was functional I added the possibility of showing only shows containing some tags or filtering only shows without others.

Overall, this was a fun project but most importantly I've learned a lot and developed something practical which I will definitely use.

##### Files:







/static/app.js - javascript for adding and removing additional input fields
/templates/index.html -  html and jinja of my webpage
/templates/layout.html - layout, links JS and bootstrap

Anime.csv - over 20 000 titles of anime with info structured like this:
ID, title, type, episodes, year, score, tags

README.md - you are here now

requirements.txt - requirements:

App.py: Flask, BeautifulSoup 4, requests, csv bot: Selenium

/bot/bot.py - bot which I have used to create anime.csv
