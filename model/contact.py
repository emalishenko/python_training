__author__ = 'emalishenko'

from sys import maxsize

class Contact:

    def __init__(self, firstname = None, middlename = None, lastname = None, nick = None,
                 homephone = None, mobilephone = None, workphone = None, secondaryphone = None, id = None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nick = nick
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.id = id

    def __repr__(self):
        return "(%s, %s, %s)" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id or other.id or self.id == other.id) \
               and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

