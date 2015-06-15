# -*- coding: utf-8 -*-


from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname = "First Name", middlename = "Middle Name", lastname = "Last Name", nick = "Nick", homephone = "+123456", mobilephone = "+89(23)347543", workphone = "346 3246734 23468", secondaryphone = "47-4378-47")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)
