#!/usr/bin/env python

import webapp2

from app.controller import app_controller
from app.controller import comment_controller

app = webapp2.WSGIApplication([
    ('/', app_controller.AppController),
    ('/comment', comment_controller.CommentController),
], debug=True)
