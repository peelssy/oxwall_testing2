from selenium.common.exceptions import NoSuchElementException
from locators.locator import InternalPageLocators as locators
from page_objects.page import Page


class InternalPage(Page):
    def is_logged_in(self):
        return self.is_element_present(locators.USER_MENU)

    def is_logged_in_as(self, user):
        return self.user_menu.text == user.username.title()

    @property
    def active_menu(self):
        return self.find_visible_element(locators.ACTIVE_MENU)

    @property
    def dashboard_menu(self):
        return self.find_visible_element(locators.DASHBOARD_MENU)

    @property
    def main_menu(self):
        return self.find_visible_element(locators.MAIN_MENU)

    # TODO Add other Nav menu

    @property
    def sign_in_menu(self):
        locator = locators.SIGN_IN_MENU
        if not self.is_logged_in():
            return self.find_visible_element(locator)
        else:
            raise NoSuchElementException("No element by locator {}".format(locator))

    @property
    def sign_up_menu(self):
        # TODO по аналогии с предыдущим
        return

    @property
    def user_menu(self):
        locator = locators.USER_MENU
        if self.is_logged_in():
            return self.find_visible_element(locator)
        else:
            raise NoSuchElementException("No element by locator {}".format(locator))

    @property
    def sign_out_link(self):
        return self.find_visible_element(locators.SIGN_OUT_LINK)

    # Nav Actions:
    def sign_out(self):
        self.action_chain.move_to_element(self.user_menu).perform()
        self.sign_out_link.click()

    def go_main_page(self):
        self.main_menu.click()

    # TODO you can do other actions that are common to all internal pages
