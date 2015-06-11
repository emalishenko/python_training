__author__ = 'emalishenko'

from model.contact import Contact
from random import randrange

def test_modify_contact_first_name(app):
    contact = Contact(first_name = "First Name Update")
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name = "To be modified", middle_name = "To be modified", last_name = "To be modified", nick = "To be modified"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.edit_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    contact.id = old_contacts[index].id
    contact.last_name = old_contacts[index].last_name
    old_contacts[index] = contact
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)



# def test_modify_first_contact_mid_name(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(first_name = "To be modified", middle_name = "To be modified", last_name = "To be modified", nick = "To be modified"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.edit_first_contact(Contact(middle_name = "Middle Name Update"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_edit_first_contact_last_name(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(first_name = "To be modified", middle_name = "To be modified", last_name = "To be modified", nick = "To be modified"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.edit_first_contact(Contact(last_name = "Last Name Update"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_edit_first_contact_nick(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(first_name = "To be modified", middle_name = "To be modified", last_name = "To be modified", nick = "To be modified"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.edit_first_contact(Contact(nick = "Nick Update"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
