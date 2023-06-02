import random
import time

from generator.generator import faker_ru
from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_new_opened_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        title_text = self.element_is_present(self.locators.TITLE_NEW).text
        return title_text

    def check_new_opened_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        title_text = self.element_is_present(self.locators.TITLE_NEW).text
        return title_text


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_appear_after_5_sec_alert(self):
        self.element_is_visible(self.locators.APPEAR_AFTER_5_SEC_BUTTON).click()
        time.sleep(6)
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_confirm_box_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        result_text = self.element_is_present(self.locators.CONFIRM_BOX_RESULT).text
        return result_text

    def check_prompt_box_alert(self):
        test_name = f'test_name{random.randint(0, 999)}'
        self.element_is_visible(self.locators.PROMPT_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(test_name)
        alert_window.accept()
        result_text = self.element_is_present(self.locators.PROMPT_BOX_RESULT).text
        return test_name, result_text