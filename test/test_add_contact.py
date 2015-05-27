# -*- coding: utf-8 -*-


from model.contact import Contact


def test_add_contact(app):
    app.session.login(user_name = "admin", password = "secret")
    app.contact.create(Contact(first_name = "First Name", middle_name = "Middle Name", last_name = "Last Name", nick = "Nick"))
    app.session.logout()

