# -*- coding: utf-8 -*-

import pytest
from application import Application
from contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(user_name = "admin", password = "secret")
    app.create_contact(Contact(first_name = "First Name", middle_name = "Middle Name", last_name = "Last Name", nick = "Nick"))
    app.logout()

