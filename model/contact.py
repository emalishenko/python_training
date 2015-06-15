__author__ = 'emalishenko'

from sys import maxsize

class Contact:

    def __init__(self, firstname = None, middlename = None, lastname = None, id = None, nick = None,
                 title = None, company = None, address = None,
                 all_phones_from_homepage = None, homephone = None, mobilephone = None, workphone = None, fax = None,
                 all_emails_from_homepage = None, email = None, email2 = None, email3 = None, homepage = None,
                 address2 = None, secondaryphone = None, notes = None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.id = id
        self.nick = nick
        self.title = title
        self.company = company
        self.address = address
        self.all_phones_from_homepage = all_phones_from_homepage
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.all_emails_from_homepage = all_emails_from_homepage
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address2 = address2
        self.secondaryphone = secondaryphone
        self.notes = notes

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

