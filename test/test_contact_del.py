__author__ = 'emalishenko'

from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name = "To be deleted", middle_name = "To be deleted", last_name = "To be deleted", nick = "To be deleted"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts [0:1] = []
    assert old_contacts == new_contacts
