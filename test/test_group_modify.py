__author__ = 'emalishenko'

from model.group import Group

def test_modify_group_name(app):
    group = Group(name="To be modified")
    if app.group.count() == 0:
        app.group.create(Group(name="New group name"))
    old_groups = app.group.get_group_list()
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)

# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(header="To be modified"))
#     app.group.modify_first_group(Group(header="New group header"))
#     old_groups = app.group.get_group_list()
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
# def test_modify_group_footer(app):
#     if app.group.count() == 0:
#         app.group.create(Group(footer="To be modified"))
#     app.group.modify_first_group(Group(footer="New group footer"))
#     old_groups = app.group.get_group_list()
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)