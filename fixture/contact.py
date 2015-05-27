__author__ = 'emalishenko'


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit new contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # click delete button
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # submit deleting
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # open contact form
        wd.find_element_by_css_selector('img[alt="Edit"]').click()
        self.fill_contact_form(contact)
        # submit contact updating
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nick)