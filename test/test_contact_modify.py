__author__ = 'emalishenko'

from model.contact import Contact

def test_edit_first_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name = "To be modified", middle_name = "To be modified", last_name = "To be modified", nick = "To be modified"))
    app.contact.edit_first_contact(Contact(first_name = "First Name Update"))


def test_edit_first_contact_mid_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name = "To be modified", middle_name = "To be modified", last_name = "To be modified", nick = "To be modified"))
    app.contact.edit_first_contact(Contact(middle_name = "Middle Name Update"))


def test_edit_first_contact_last_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name = "To be modified", middle_name = "To be modified", last_name = "To be modified", nick = "To be modified"))
    app.contact.edit_first_contact(Contact(last_name = "Last Name Update"))


def test_edit_first_contact_nick(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name = "To be modified", middle_name = "To be modified", last_name = "To be modified", nick = "To be modified"))
    app.contact.edit_first_contact(Contact(nick = "Nick Update"))
