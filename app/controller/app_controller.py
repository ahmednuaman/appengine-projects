#!/usr/bin/env python

import jinja2
import webapp2

from app.model import comment_model

class AppController(webapp2.RequestHandler):
    def get(self):
        # get our template
        template = get_template({
            'comments' : comment_model.get_comments()
        })

        # return it to the browser
        self.response.out.write(template)


def get_template(data):
    # prepare our templating engine
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('app/view/'))

    # get our template
    template = env.get_template('app.html')

    # render our template
    return template.render(data)
