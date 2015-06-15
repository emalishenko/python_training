# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import string
import random
import re

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone(prefix, maxlen):
    phone = string.digits + "()-+ /"
    return prefix + "".join([random.choice(phone) for i in range(maxlen)])

testdata = [Contact(firstname = random_string("first", 20),
                    middlename = random_string("middle", 20),
                    lastname = random_string("las", 20),
                    nick = random_string("nick", 10),
                    title = random_string("title", 20),
                    company = random_string("company", 15),
                    address = random_string("addr", 40),
                    homephone = random_phone("h-ph", 8),
                    mobilephone = random_phone("m-ph", 8),
                    workphone = random_phone("w-ph", 8),
                    fax = random_phone("fax", 8),
                    email2 = random_string("email2", 20),
                    email3 = random_string("email3", 20),
                    homepage = random_string("homepage", 20),
                    address2 = random_string("addr2", 20),
                    secondaryphone = random_phone("ph-2", 8),
                    notes = random_string("notes", 50))
            for i in range(3)]

@pytest.mark.parametrize("contact", testdata, ids = [repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    contact.lastname = re.sub("\s+", " ", contact.lastname).strip()
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)
