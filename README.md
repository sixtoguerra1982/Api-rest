## Funx Backend developer test 

This is a simple software test is designed to know the way as you resolve a simple problem using software.

We are looking for candidates who really enjoy codign and try to make the most reausable softwares elements.

## The problem

In Funx it's a everyday work design and implement differents kinds of endpoints to be consumed by massively downloaded mobile apps.

In this case you must help our client Teleton Chile to have a copy of their news feed for their wordpress site on the Aplicatón (Teleton's App).

Teleton wants to allow the users to comment and like the posts from their feed, so you must find the way to build a simple solution that go for the Teleton news feed and allow the users to comment and like the different posts through the app.

##We need to expose JSON REST endpoints to allow the users to:
* See the news feed.
* Like a post.
* Comment a post.


## Minimum objectives

* Parse feed in json 
* Model Database to store items from feed
* Model additional items in database to support likes and comments for items 
* Code API REST to list items
* Code API REST to recept comments for items
* Code API REST to recept likes

## Considerations

* Comments and likes can be anonymous (But you can assume and user_id instead it's the same)
* You don't need to expose the user's name on the comment or like.
* Frameworks to be used: You may use Ruby (Rails, Sinatra) or Python(Django or Flask).

## Teleton's newsfeed endpoint:

    https://www.teleton.cl/feed/?json


## Delivery instructions 

After than you finish your development you have to make a pull request in this repository. This one will be review for us and then will be rejected.
