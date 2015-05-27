__author__ = 'emalishenko'

from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(user_name="admin", password="secret")
    app.contact.edit_first_contact(Contact(first_name = "First Name Update", middle_name = "Middle Name Update", last_name = "Last Name Update", nick = "Nick Update"))
    app.session.logout()