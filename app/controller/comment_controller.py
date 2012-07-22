#!/usr/bin/env python

import json
import webapp2

from app.model import comment_model

class CommentController(webapp2.RequestHandler):
    def get(self):
        # get our comments
        comments = comment_model.get_comments()

        # encode them as json
        comments = json.dumps(comments)

        # return them to the browser
        self.response.out.write(comments)
    
    def post(self):
        # save a comment
        response = comment_model.add_comment(self.request.get('author'), self.request.get('comment'))

        # encode the response
        response = json.dumps(response)

        # return a response
        self.response.out.write(response)
    
