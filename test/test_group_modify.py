__author__ = 'emalishenko'

from model.group import Group

def test_modify_group_name(app):
    app.session.login(user_name="admin", password="secret")
    app.group.modify_first_group(Group(name="New group name"))
    app.session.logout()

def test_modify_group_header(app):
    app.session.login(user_name="admin", password="secret")
    app.group.modify_first_group(Group(header="New group header"))
    app.session.logout()

def test_modify_group_footer(app):
    app.session.login(user_name="admin", password="secret")
    app.group.modify_first_group(Group(footer="New group footer"))
    app.session.logout()