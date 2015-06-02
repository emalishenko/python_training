__author__ = 'emalishenko'

from model.group import Group

def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="New group name"))

def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="New group header"))

def test_modify_group_footer(app):
    app.group.modify_first_group(Group(footer="New group footer"))