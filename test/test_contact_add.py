# -*- coding: utf-8 -*-


from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(first_name = "First Name", middle_name = "Middle Name", last_name = "Last Name", nick = "Nick"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
