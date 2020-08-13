from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Category, AuctionListing, Bid, Comment

import datetime as dt


def index(request):
    obj = AuctionListing.objects.all()
    return render(request, "auctions/index.html", {
        "objects": obj
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def createListing(request):
    if request.method == 'POST':
        title = request.POST["title"]
        date = dt.datetime.now()
        description = request.POST["description"]
        startBid = request.POST["startBid"]
        imageUrl = request.POST["url"]
        category = Category.objects.get(id=request.POST["category"])
        user = User.objects.get(username=request.POST["user"])
        listing = AuctionListing.objects.create(
            name=title, category=category, date=date, startBid=startBid, description=description, user=user, imageUrl=imageUrl)
        listing.save()
        return HttpResponseRedirect(reverse("index"))
    return render(request, "auctions/createListing.html", {
        'categories': Category.objects.all()
    })


def details(request, id, message=None):
    item = AuctionListing.objects.get(id=id)
    bids = Bid.objects.filter(auctionListing=item)
    comments = Comment.objects.filter(auctionListing=item)
    return render(request, "auctions/details.html", {
        'item': item,
        'bids': bids,
        'comments': comments,
        'message': message
    })


def categories(request):
    return render(request, "auctions/categories.html", {
        'categories': Category.objects.all()
    })


def filter(request, name):
    category = Category.objects.get(name=name)
    obj = AuctionListing.objects.filter(category=category)
    return render(request, "auctions/index.html", {
        "objects": obj
    })


def comment(request, id):
    if request.method == 'POST':
        auctionListing = AuctionListing.objects.get(id=id)
        user = User.objects.get(username=request.POST["user"])
        commentValue = request.POST["content"]
        comment = Comment.objects.create(date=dt.datetime.now(
        ), user=user, auctionListing=auctionListing, commentValue=commentValue)
        comment.save()
        return HttpResponseRedirect(reverse("details", kwargs={'id': id}))
    return HttpResponseRedirect(reverse("index"))


def bid(request, id):
    if request.method == 'POST':
        auctionListing = AuctionListing.objects.get(id=id)
        bidValue = request.POST["bid"]
        for i in Bid.objects.filter(auctionListing=auctionListing):
            if i.bidValue > int(bidValue):
                return details(request, id, message="Place a Higher Bid!")
        user = User.objects.get(username=request.POST["user"])
        date = dt.datetime.now()
        bid = Bid.objects.create(
            date=date, user=user, bidValue=bidValue, auctionListing=auctionListing)
        bid.save()
        return HttpResponseRedirect(reverse("details", kwargs={'id': id}))
    return HttpResponseRedirect(reverse("index"))
