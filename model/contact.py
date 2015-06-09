__author__ = 'emalishenko'

from sys import maxsize

class Contact:

    def __init__(self, first_name = None, middle_name = None, last_name = None, nick = None, id = None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nick = nick
        self.id = id

    def __repr__(self):
        return "(%s, %s, %s)" % (self.id, self.last_name, self.first_name)

    def __eq__(self, other):
        return (self.id or other.id or self.id == other.id) and self.first_name == other.first_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

