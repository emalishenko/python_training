__author__ = 'emalishenko'


class Contact:

    def __init__(self, first_name = None, middle_name = None, last_name = None, nick = None, id = None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nick = nick
        self.id = id

    def __repr__(self):
        return "(%s, %s)" % (self.id, self.first_name)

    def __eq__(self, other):
        return self.id == other.id and self.first_name == other.first_name

