__author__ = 'Administrator'
import tornado.web as WEB
import os
from model import *

db = DataBase()
class HomeHandler(WEB.RequestHandler):
    def get(self):
        records =  db.find_all("person_info",None);
        infos = {}
        index = 0
        for record in records:
            infos[index] = [record["url"], record["title"], record["desc"]]
            index += 1
        #infos = {}
        return self.render("home.html", infos = infos)