from google.appengine.ext import ndb

class Sporocilo(ndb.Model):
    ime = ndb.StringProperty()
    mail = ndb.StringProperty()
    sporocilo = ndb.StringProperty()
    nastanek = ndb.DateTimeProperty(auto_now_add=True)