__author__ = 'emalishenko'

from model.contact import Contact
from random import randrange


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname = "First Name", middlename = "Middle Name", lastname = "Last Name",
                                   nick = "Nick", homephone = "+123456", mobilephone = "+89(23)347543",
                                   workphone = "346 3246734 23468", secondaryphone = "47-4378-47"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts [index:index+1] = []
    assert old_contacts == new_contacts
