#!/usr/bin/env python

from google.appengine.ext import db

class CommentModel(db.Model):
    author = db.StringProperty()
    comment = db.TextProperty()
    submitted = db.DateTimeProperty(auto_now_add=True)

def get_comments():
    # return all the comments from our database
    comments = []

    # run a query
    query = CommentModel.all()

    # loop through the query and append the comments to our list
    for comment in query:
        comments.append({
            'author': comment.author,
            'comment': comment.comment
        })

    # return the comments
    return comments

def add_comment(author, comment):
    # simply add the comment to our database
    entry = CommentModel()

    # assign the values
    entry.author = author
    entry.comment = comment

    # save its ass
    return bool(entry.put())
