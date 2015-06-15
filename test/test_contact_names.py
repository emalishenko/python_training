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
    assert contact_from_homepage.firstname == clear(contact_from_editpage.firstname)
    assert contact_from_homepage.lastname == clear(contact_from_editpage.lastname)
    assert contact_from_homepage.address == clear(app.contact.format_fields_like_on_homepage(
        contact_from_editpage.address.split("\n")))


def clear(s):
     return re.sub("\s{2,}", " ", s)




