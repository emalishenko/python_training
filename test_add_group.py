# -*- coding: utf-8 -*-

import pytest
from application import Application
from group import Group

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(user_name="admin", password="secret")
    app.create_group(Group(name="Test Grop1", header="Header text1", footer="Footer text1"))
    app.logout()


def test_add_empty_group(app):
    app.login(user_name="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

