# Auction

![Github Followers](https://img.shields.io/github/followers/shaw8wit?label=Follow&style=plastic)
![GitHub stars](https://img.shields.io/github/stars/shaw8wit/Auction?style=plastic)
![GitHub forks](https://img.shields.io/github/forks/shaw8wit/Auction?style=plastic)
![GitHub watchers](https://img.shields.io/github/watchers/shaw8wit/Auction?style=plastic)

![Demo Screen](https://github.com/shaw8wit/Auction/blob/master/screenshots/watchlist.png)

A fully functional Auction website in Django. With configured admin panel.

View all screenshots [here](https://github.com/shaw8wit/Auction/blob/master/screenshots/)

## About
+ This is a dummy-website for holding Auctions.
+ Users can view listings, its bids and comments without signing in.
+ To place a Listing for auction and to bid on other auctions users have to register and login.
+ In addition to the above users can also add listings to watchlist.
+ A listings bidding can be stopped only by its author at any time making it inactive.
+ The inactive listing is same as the active one except that the bidding has now stopped.
+ Users can add categories and filter listings according to the categories.
+ Appropriate alert messages are shown for actions.

## Database
+ Connect any relational database or use the built in SQLite database.
+ ORM's have been used for all database queries

## Getting Started
+ clone or download the repo and ```cd``` into the directory.
+ Run ```python manage.py makemigrations auctions``` to make migrations for the ```auctions``` app.
+ Run ```python manage.py migrate``` to apply migrations to your database.
+ Run ```python manage.py runserver``` to run the server in your local machine.
