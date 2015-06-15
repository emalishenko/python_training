__author__ = 'emalishenko'

import re

def test_phones_on_home_page(app):
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_editpage = app.contact.get_contact_info_from_edit_page(0)
    all_phones_from_editpage = [contact_from_editpage.homephone, contact_from_editpage.mobilephone,
                                contact_from_editpage.workphone, contact_from_editpage.secondaryphone]
    assert contact_from_homepage.all_phones_from_homepage == app.contact.format_fields_like_on_homepage(
        clear(all_phones_from_editpage))

# def test_phones_on_contact_view_page(app):
#     contact_from_view_page = app.contact.get_contact_from_view_page(0)
#     contact_from_editpage = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_view_page.homephone == contact_from_editpage.homephone
#     assert contact_from_view_page.workphone == contact_from_editpage.workphone
#     assert contact_from_view_page.mobilephone == contact_from_editpage.mobilephone
#     assert contact_from_view_page.secondaryphone == contact_from_editpage.secondaryphone

def clear(l):
    return map(lambda x: re.sub("[/() -]", "", x), l)

# def merge_phones_like_on_homepage(contact):
#     return "\n".join(filter(lambda x: x != "",
#                      (map(lambda x: clear(x),
#                           filter(lambda x: x is not None, [contact.homephone, contact.mobilephone,
#                                                           contact.workphone, contact.secondaryphone])))))




