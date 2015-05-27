__author__ = 'emalishenko'


from model.group import Group


def test_edit_first_group(app):
    app.session.login(user_name="admin", password="secret")
    app.group.edit_first_group(Group(name="Test Grop Update", header="Header text update", footer="Footer text update"))
    app.session.logout()

