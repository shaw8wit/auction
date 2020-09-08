# Auction
A fully functional Auction website in Django. With configured admin panel.

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
+ Run ```python manage.py makemigrations auctions``` to make migrations for the ```mail``` app.
+ Run ```python manage.py migrate``` to apply migrations to your database.
+ Run ```python manage.py runserver``` to run the server in your local machine.
