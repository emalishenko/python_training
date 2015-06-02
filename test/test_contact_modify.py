__author__ = 'emalishenko'

from model.contact import Contact

def test_edit_first_contact_name(app):
    app.contact.edit_first_contact(Contact(first_name = "First Name Update"))
    app.session.logout()


def test_edit_first_contact_mid_name(app):
    app.contact.edit_first_contact(Contact(middle_name = "Middle Name Update"))


def test_edit_first_contact_last_name(app):
    app.contact.edit_first_contact(Contact(last_name = "Last Name Update"))


def test_edit_first_contact_nick(app):
    app.contact.edit_first_contact(Contact(nick = "Nick Update"))
