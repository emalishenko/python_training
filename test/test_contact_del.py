__author__ = 'emalishenko'

from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name = "To be deleted", middle_name = "To be deleted", last_name = "To be deleted", nick = "To be deleted"))
    app.contact.delete_first_contact()
