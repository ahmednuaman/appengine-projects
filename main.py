#!/usr/bin/env python

import webapp2

from app.controller.app_controller import AppController
from app.controller.app_controller import CommentController

app = webapp2.WSGIApplication([
    ('/', AppController),
    ('/comment', CommentController),
], debug=True)
