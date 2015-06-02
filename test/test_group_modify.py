__author__ = 'emalishenko'

from model.group import Group

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="To be modified"))
    app.group.modify_first_group(Group(name="New group name"))

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="To be modified"))
    app.group.modify_first_group(Group(header="New group header"))

def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="To be modified"))
    app.group.modify_first_group(Group(footer="New group footer"))