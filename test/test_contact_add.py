# -*- coding: utf-8 -*-


from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(first_name = "First Name", middle_name = "Middle Name", last_name = "Last Name", nick = "Nick"))

