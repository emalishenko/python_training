__author__ = 'emalishenko'


from fixture.contact import Contact
from random import randrange
import re

def test_name_on_homepage(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname = "First Name", middlename = "Middle Name", lastname = "Last Name",
                                   nick = "Nick", homephone = "+123456", mobilephone = "+89(23)347543",
                                   workphone = "346 3246734 23468", secondaryphone = "47-4378-47"))
    contact_list = app.contact.get_contact_list()
    index = randrange(len(contact_list))
    contact_from_homepage = contact_list[index]
    contact_from_editpage = app.contact.get_contact_info_from_edit_page(index)
    all_emails_from_edit_page = [contact_from_editpage.email, contact_from_editpage.email2, contact_from_editpage.email3]
    assert contact_from_homepage.all_emails_from_homepage == app.contact.format_fields_like_on_homepage(clear(
        all_emails_from_edit_page))


def clear(list):
     return map(lambda x: re.sub("\s{2,}", " ", x), list)