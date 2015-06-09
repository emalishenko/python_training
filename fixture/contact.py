__author__ = 'emalishenko'

from model.contact import Contact

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
        self.select_first_contact()
        # click delete button
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # submit deleting
        wd.switch_to_alert().accept()
        self.open_homepage()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.select_first_contact()
        # open contact form
        wd.find_element_by_css_selector('img[alt="Edit"]').click()
        self.fill_contact_form(contact)
        # submit contact updating
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("nickname", contact.nick)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    def open_homepage(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php")):
            wd.find_element_by_link_text("home").click()

    def get_contact_list(self):
        wd = self.app.wd
        self.open_homepage()
        contacts = []
        all_entries = wd.find_elements_by_name("entry")
        row_number = 2
        for element in all_entries:
            id = element.find_element_by_name("selected[]").get_attribute("value")
            last_name = element.find_element_by_xpath("//table[@id='maintable']/tbody/tr[%s]/td[2]" % (row_number)).text
            first_name = element.find_element_by_xpath("//table[@id='maintable']/tbody/tr[%s]/td[3]" % (row_number)).text
            contacts.append(Contact(first_name = first_name, last_name = last_name, id = id))
            row_number += 1
        return contacts
