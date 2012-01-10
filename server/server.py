#!/usr/bin/env python
# encoding: utf-8
"""
server.py

Created by Peter Ma on 2012-01-05.
Copyright (c) 2012 Maven Studio. All rights reserved.
"""
import tornado.autoreload

import tornado.httpserver
import logging
import tornado.auth
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import os.path
import uuid
import tornado.database

import weiboauth

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)
define("mysql_host", default="127.0.0.1:3306", help="server database host")
define("mysql_database", default="freelunch", help="server database name")
define("mysql_user", default="root", help="server database user")
define("mysql_password", default="suame806", help="server database password")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/auth/login", AuthLoginHandler),
            (r"/auth/logout", AuthLogoutHandler),
            (r"/a/message/new", MessageNewHandler),
            (r"/a/message/updates", MessageUpdatesHandler),
            (r"/user/update", UserUpdateHander),
            (r"/user/list",UsersListHandler),
            
        ]
        settings = dict(
            cookie_secret="43oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            login_url="/auth/login",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
            weibo_consumer_key="3331857532",
            weibo_consumer_secret="0a965b08dd9754165e5fa98348e15959"
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        
        # Have one global connection to the blog DB across all handlers
        self.db = tornado.database.Connection(
            host=options.mysql_host, database=options.mysql_database,
            user=options.mysql_user, password=options.mysql_password)



class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db
    
    
    def get_current_user(self):
        user_json = self.get_secure_cookie("user")
        if not user_json: return None
        return tornado.escape.json_decode(user_json)


class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("index.html", messages=MessageMixin.cache)


class MessageMixin(object):
    waiters = []
    cache = []
    cache_size = 200

    def wait_for_messages(self, callback, cursor=None):
        cls = MessageMixin
        if cursor:
            index = 0
            for i in xrange(len(cls.cache)):
                index = len(cls.cache) - i - 1
                if cls.cache[index]["id"] == cursor: break
            recent = cls.cache[index + 1:]
            if recent:
                callback(recent)
                return
        cls.waiters.append(callback)

    def new_messages(self, messages):
        cls = MessageMixin
        logging.info("Sending new message to %r listeners", len(cls.waiters))
        for callback in cls.waiters:
            try:
                callback(messages)
            except:
                logging.error("Error in waiter callback", exc_info=True)
        cls.waiters = []
        cls.cache.extend(messages)
        if len(cls.cache) > self.cache_size:
            cls.cache = cls.cache[-self.cache_size:]


class MessageNewHandler(BaseHandler, MessageMixin):
    @tornado.web.authenticated
    def post(self):
        '''pdb.set_trace()
        '''
        message = {
            "id": str(uuid.uuid4()),
            "from": self.current_user["username"],
            "body": self.get_argument("body"),
        }
        message["html"] = self.render_string("message.html", message=message)
        if self.get_argument("next", None):
            self.redirect(self.get_argument("next"))
        else:
            self.write(message)
        self.new_messages([message])


class MessageUpdatesHandler(BaseHandler, MessageMixin):
    @tornado.web.authenticated
    @tornado.web.asynchronous
    def post(self):
        cursor = self.get_argument("cursor", None)
        self.wait_for_messages(self.async_callback(self.on_new_messages),
                               cursor=cursor)

    def on_new_messages(self, messages):
        # Closed client connection
        if self.request.connection.stream.closed():
            return
        self.finish(dict(messages=messages))


class AuthLoginHandler(BaseHandler, weiboauth.WeiboMixin):
    @tornado.web.asynchronous
    def get(self):
        if self.get_argument("oauth_token", None):
            self.get_authenticated_user(self.async_callback(self._on_auth))
            return
        
        callback_url = "%s://%s%s" % (self.request.protocol,
                                      self.request.host,
                                      self.get_login_url())
        self.authorize_redirect(callback_url)

    def _on_auth(self, user):
        if not user:
            raise tornado.web.HTTPError(500, "Weibo auth failed")
        self.set_secure_cookie("user", tornado.escape.json_encode(user))
        self.redirect("/")


class AuthLogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.write("You are now logged out")


class UserUpdateHander(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        try:
            self.db.execute("INSERT INTO users (name,password) VALUES(%s,%s)",self.current_user["username"],'password')
        except:
            self.render("users.html", entry='database operate meets exception.')                
        entry = self.db.get("SELECT * FROM users limit 1")
        self.render("users.html", entry=entry)   

class UsersListHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        users = self.db.query("select * from users")
        self.render("users_list.html",users = users) 
        
        
        
def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

def develop():
    app = Application()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(8888)
    instance = tornado.ioloop.IOLoop.instance()
    tornado.autoreload.start(instance)
    instance.start()

if __name__ == "__main__":
    # main()
    develop()

